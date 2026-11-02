//! Browser admission and faithful projection over LUCIA's unchanged native core.
use lucia_history_core::{
    compare_to_established, validate_history, EstablishedStoryProfile, PeopleHistory,
};
use serde::{de::DeserializeOwned, Deserialize};
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use wasm_bindgen::prelude::*;

pub const MAX_REQUEST_BYTES: usize = 2_097_152;
pub const MAX_HISTORY_BYTES: usize = 262_144;
pub const MAX_PROFILE_BYTES: usize = 131_072;
pub const MAX_REPORT_BYTES: usize = 2_097_152;

#[derive(Deserialize)]
#[serde(rename_all = "snake_case")]
enum Operation {
    Validate,
    Compare,
}
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
struct Request {
    operation: Operation,
    history_json: String,
    #[serde(default)]
    profile_json: Option<String>,
}

fn error(kind: &str, message: impl ToString) -> Value {
    json!({"kind":kind,"message":message.to_string()})
}
fn hash(text: &str) -> String {
    format!("{:x}", Sha256::digest(text.as_bytes()))
}
fn decode<T: DeserializeOwned>(text: &str) -> Result<(T, Vec<String>, usize), serde_json::Error> {
    let mut decoder = serde_json::Deserializer::from_str(text);
    let mut ignored = Vec::new();
    let mut count = 0;
    let value = serde_ignored::deserialize(&mut decoder, |path| {
        count += 1;
        if ignored.len() < 1024 {
            ignored.push(path.to_string());
        }
    })?;
    decoder.end()?;
    Ok((value, ignored, count))
}
fn string_bound(value: &Value) -> bool {
    match value {
        Value::String(s) => s.len() <= 4096,
        Value::Array(a) => a.iter().all(string_bound),
        Value::Object(o) => o.values().all(string_bound),
        _ => true,
    }
}
fn analyze(text: &str) -> Value {
    if text.len() > MAX_REQUEST_BYTES {
        return error(
            "browser_refusal",
            "Request exceeds 2 MiB UTF-8; native CLI size limits are separate.",
        );
    }
    let request: Request = match serde_json::from_str(text) {
        Ok(r) => r,
        Err(e) => return error("invalid_request", e),
    };
    if request.history_json.len() > MAX_HISTORY_BYTES {
        return error("browser_refusal", "History exceeds 256 KiB UTF-8.");
    }
    let (history, history_ignored, history_ignored_count): (PeopleHistory, _, _) =
        match decode(&request.history_json) {
            Ok(r) => r,
            Err(e) => return error("invalid_history_json", e),
        };
    let history_known = serde_json::to_value(&history).expect("Native serializable history");
    let eras = history.eras.len();
    let persons: usize = history.eras.iter().map(|e| e.persons.len()).sum();
    let events: usize = history.eras.iter().map(|e| e.events.len()).sum();
    let refs = history.source_story_refs.len()
        + history
            .eras
            .iter()
            .map(|e| {
                e.source_story_refs.len()
                    + e.persons
                        .iter()
                        .map(|p| p.source_story_refs.len())
                        .sum::<usize>()
                    + e.events
                        .iter()
                        .map(|v| v.source_story_refs.len())
                        .sum::<usize>()
            })
            .sum::<usize>();
    let actor_places: usize = history
        .eras
        .iter()
        .flat_map(|e| &e.events)
        .map(|e| e.actors.len() + e.places.len())
        .sum();
    if eras > 32
        || persons > 256
        || events > 512
        || refs > 2048
        || actor_places > 4096
        || history.framing_notes.len() > 128
        || history_ignored_count > 1024
        || !string_bound(&history_known)
    {
        return error("browser_refusal","History scope: at most 32 eras, 256 persons, 512 events, 2048 references, 4096 actor/place entries, 128 framing notes, 1024 ignored fields and 4096 UTF-8 bytes per interpreted string.");
    }
    let findings = validate_history(&history);
    let errors = findings
        .iter()
        .filter(|f| f.severity == lucia_history_core::FindingSeverity::Error)
        .count();
    let warnings = findings.len() - errors;
    let mut profile_known = Value::Null;
    let mut profile_ignored = Vec::new();
    let mut profile_hash = Value::Null;
    let mut comparison = Value::Null;
    let comparing = matches!(request.operation, Operation::Compare);
    if comparing {
        let Some(raw) = request.profile_json.as_deref() else {
            return error(
                "invalid_request",
                "Compare requires profile_json; history-only validation does not use it.",
            );
        };
        if raw.len() > MAX_PROFILE_BYTES {
            return error("browser_refusal", "Profile exceeds 128 KiB UTF-8.");
        }
        let (profile, ignored, count): (EstablishedStoryProfile, _, _) = match decode(raw) {
            Ok(r) => r,
            Err(e) => return error("invalid_profile_json", e),
        };
        profile_known = serde_json::to_value(&profile).expect("Native serializable profile");
        if profile.required_event_ids.len() > 512
            || profile.required_person_ids.len() > 512
            || profile.required_story_paths.len() > 512
            || profile.forbidden_external_framings.len() > 128
            || count > 1024
            || !string_bound(&profile_known)
        {
            return error("browser_refusal","Profile scope: at most 512 entries per required list, 128 framing patterns, 1024 ignored fields and 4096 UTF-8 bytes per interpreted string.");
        }
        comparison = serde_json::to_value(compare_to_established(&history, &profile))
            .expect("Native serializable comparison");
        profile_hash = json!(hash(raw));
        profile_ignored = ignored;
    }
    json!({"kind":"report","schema":"lucia.history-inspector.v1","operation":if comparing{"compare"}else{"validate"},
        "request_sha256":hash(text),"history_sha256":hash(&request.history_json),"profile_sha256":profile_hash,
        "counts":{"eras":eras,"persons":persons,"events":events,"reference_entries":refs,"error_findings":errors,"warning_findings":warnings},
        "findings":findings,"comparison":comparison,"interpreted_history":history_known,"interpreted_profile":profile_known,
        "ignored_history_fields":history_ignored,"ignored_profile_fields":profile_ignored,
        "projection_notice":"Interpreted fields are the native typed view: defaults may materialize and ignored extensions are omitted. Original/current/request downloads retain supplied text; this report is not a replacement source record. Ignored paths use Serde notation, not JSON Pointer.",
        "scope":"Structural checks against caller-supplied records/profile only. No source paths are opened or verified; no historical truth, causal mechanism, chapter/manuscript/board approval, rubric rescoring or generic history contract follows.",
        "native_limits":"Native does not prove ID uniqueness, event-container/era agreement, nonempty requirements, source existence or all prose framing. Comparison can pass with warnings or empty coverage. Framing scan is case-insensitive substring matching on framing_notes only, including empty patterns.",
        "profile_used":comparing})
}

#[wasm_bindgen]
pub fn inspect_request(text: &str) -> String {
    let result = analyze(text).to_string();
    if result.len() > MAX_REPORT_BYTES {
        error("browser_refusal", "Report exceeds 2 MiB.").to_string()
    } else {
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    fn history() -> Value {
        json!({"people_id":"demo-people","title":"Synthetic record","worldview":"Software example, not an account of real people.","eras":[{"era_id":"demo-era","title":"Demo era","persons":[{"person_id":"p1","display_name":"Demo person","role":"Illustrative role","source_story_refs":[{"path":"synthetic/chapter.md"}]}],"events":[{"event_id":"e1","era_id":"demo-era","title":"Demo event","event_kind":"example","consequence":"An input claim, not demonstrated causality.","actors":["p1"],"source_story_refs":[{"path":"synthetic/chapter.md"}]}]}]})
    }
    fn profile() -> Value {
        json!({"profile_id":"demo-profile","required_event_ids":["e1"],"required_person_ids":["p1"],"required_story_paths":["synthetic/chapter.md"],"forbidden_external_framings":["forbidden-demo"]})
    }
    fn request(h: Value, p: Value) -> String {
        json!({"operation":"compare","history_json":h.to_string(),"profile_json":p.to_string()})
            .to_string()
    }
    #[test]
    fn exactly_projects_native_findings_and_comparison() {
        let h = history();
        let p = profile();
        let raw = request(h.clone(), p.clone());
        let r = analyze(&raw);
        let history: PeopleHistory = serde_json::from_value(h).unwrap();
        let profile: EstablishedStoryProfile = serde_json::from_value(p).unwrap();
        assert_eq!(
            r["findings"],
            serde_json::to_value(validate_history(&history)).unwrap()
        );
        assert_eq!(
            r["comparison"],
            serde_json::to_value(compare_to_established(&history, &profile)).unwrap()
        );
        assert_eq!(inspect_request(&raw), inspect_request(&raw));
        assert_eq!(r["request_sha256"], hash(&raw));
    }
    #[test]
    fn extensions_and_duplicate_recognized_fields_keep_native_parser_behavior() {
        let mut h = history();
        h["extension"] = json!({"keep":"original only"});
        h["eras"][0]["events"][0]["extra"] = json!(1);
        let r = analyze(&request(h.clone(), profile()));
        assert_eq!(r["ignored_history_fields"].as_array().unwrap().len(), 2);
        assert!(r["interpreted_history"].get("extension").is_none());
        let raw = h
            .to_string()
            .replacen("{", "{\"people_id\":\"duplicate\",", 1);
        let direct = serde_json::from_str::<PeopleHistory>(&raw)
            .unwrap_err()
            .to_string();
        let wrapped = analyze(&json!({"operation":"validate","history_json":raw}).to_string());
        assert_eq!(wrapped["message"], direct);
    }
    #[test]
    fn warning_only_pass_empty_coverage_and_native_framing_limits_are_explicit() {
        let mut h = history();
        h["eras"][0]["events"][0]["actors"] = json!(["unknown"]);
        let r = analyze(&request(h, profile()));
        assert_eq!(r["comparison"]["status"], "pass");
        assert_eq!(r["counts"]["warning_findings"], 1);
        let empty = json!({"people_id":"demo","title":"Empty","worldview":"Synthetic"});
        let r = analyze(&request(empty, json!({"profile_id":""})));
        assert_eq!(r["comparison"]["status"], "pass");
        assert_eq!(r["counts"]["events"], 0);
        let mut h = history();
        h["framing_notes"] = json!(["FORBIDDEN-DEMO"]);
        assert_eq!(
            analyze(&request(h, profile()))["comparison"]["status"],
            "hold"
        );
    }
    #[test]
    fn mode_and_resource_boundaries_are_separate_from_native_errors() {
        let r=analyze(&json!({"operation":"validate","history_json":history().to_string(),"profile_json":"{"}).to_string());
        assert_eq!(r["kind"], "report");
        assert_eq!(r["profile_used"], false);
        assert_eq!(
            analyze(&" ".repeat(MAX_REQUEST_BYTES + 1))["kind"],
            "browser_refusal"
        );
        let mut h = history();
        h["title"] = json!("x".repeat(4097));
        assert_eq!(analyze(&request(h, profile()))["kind"], "browser_refusal");
        assert_eq!(
            analyze(&json!({"operation":"validate","history_json":"{"}).to_string())["kind"],
            "invalid_history_json"
        );
    }
}
