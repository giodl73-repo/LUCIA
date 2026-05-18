use serde::{Deserialize, Serialize};
use std::collections::{BTreeSet, HashSet};

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct PeopleHistory {
    pub people_id: String,
    pub title: String,
    pub worldview: String,
    #[serde(default)]
    pub framing_notes: Vec<String>,
    #[serde(default)]
    pub eras: Vec<EraHistory>,
    #[serde(default)]
    pub source_story_refs: Vec<StoryRef>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct EraHistory {
    pub era_id: String,
    pub title: String,
    #[serde(default)]
    pub persons: Vec<Person>,
    #[serde(default)]
    pub events: Vec<HistoryEvent>,
    #[serde(default)]
    pub source_story_refs: Vec<StoryRef>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct Person {
    pub person_id: String,
    pub display_name: String,
    pub role: String,
    #[serde(default)]
    pub source_story_refs: Vec<StoryRef>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct HistoryEvent {
    pub event_id: String,
    pub era_id: String,
    pub title: String,
    pub event_kind: String,
    pub consequence: String,
    #[serde(default)]
    pub year_label: Option<String>,
    #[serde(default)]
    pub actors: Vec<String>,
    #[serde(default)]
    pub places: Vec<String>,
    #[serde(default)]
    pub source_story_refs: Vec<StoryRef>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct StoryRef {
    pub path: String,
    #[serde(default)]
    pub anchor: Option<String>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct EstablishedStoryProfile {
    pub profile_id: String,
    #[serde(default)]
    pub required_event_ids: Vec<String>,
    #[serde(default)]
    pub required_person_ids: Vec<String>,
    #[serde(default)]
    pub required_story_paths: Vec<String>,
    #[serde(default)]
    pub forbidden_external_framings: Vec<String>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct ComparisonReport {
    pub profile_id: String,
    pub status: ComparisonStatus,
    pub missing_event_ids: Vec<String>,
    pub missing_person_ids: Vec<String>,
    pub missing_story_paths: Vec<String>,
    pub uncited_event_ids: Vec<String>,
    pub uncited_person_ids: Vec<String>,
    pub external_framing_flags: Vec<String>,
    pub findings: Vec<HistoryFinding>,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ComparisonStatus {
    Pass,
    Hold,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct HistoryFinding {
    pub severity: FindingSeverity,
    pub code: String,
    pub location: String,
    pub message: String,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum FindingSeverity {
    Error,
    Warning,
}

pub fn validate_history(history: &PeopleHistory) -> Vec<HistoryFinding> {
    let mut findings = Vec::new();

    require_non_empty(
        &mut findings,
        "people_id",
        "people.people_id",
        &history.people_id,
    );
    require_non_empty(&mut findings, "title", "people.title", &history.title);
    require_non_empty(
        &mut findings,
        "worldview",
        "people.worldview",
        &history.worldview,
    );

    let era_ids: HashSet<&str> = history.eras.iter().map(|era| era.era_id.as_str()).collect();
    let person_ids: HashSet<&str> = history
        .eras
        .iter()
        .flat_map(|era| era.persons.iter().map(|person| person.person_id.as_str()))
        .collect();

    for era in &history.eras {
        require_non_empty(&mut findings, "era_id", "era.era_id", &era.era_id);
        require_non_empty(&mut findings, "era_title", &era.era_id, &era.title);

        for person in &era.persons {
            require_non_empty(
                &mut findings,
                "person_id",
                &format!("{}.person", era.era_id),
                &person.person_id,
            );
            require_non_empty(
                &mut findings,
                "person_name",
                &person.person_id,
                &person.display_name,
            );
            require_non_empty(
                &mut findings,
                "person_role",
                &person.person_id,
                &person.role,
            );
            if person.source_story_refs.is_empty() {
                findings.push(warning(
                    "person_uncited",
                    &person.person_id,
                    "person has no established-story reference",
                ));
            }
        }

        for event in &era.events {
            require_non_empty(
                &mut findings,
                "event_id",
                &format!("{}.event", era.era_id),
                &event.event_id,
            );
            require_non_empty(&mut findings, "event_title", &event.event_id, &event.title);
            require_non_empty(
                &mut findings,
                "event_kind",
                &event.event_id,
                &event.event_kind,
            );
            require_non_empty(
                &mut findings,
                "event_consequence",
                &event.event_id,
                &event.consequence,
            );
            if !era_ids.contains(event.era_id.as_str()) {
                findings.push(error(
                    "event_unknown_era",
                    &event.event_id,
                    "event references an era_id that does not exist in this people history",
                ));
            }
            for actor in &event.actors {
                if !person_ids.contains(actor.as_str()) {
                    findings.push(warning(
                        "event_unknown_actor",
                        &event.event_id,
                        &format!("event actor `{actor}` is not listed as a person"),
                    ));
                }
            }
            if event.source_story_refs.is_empty() {
                findings.push(warning(
                    "event_uncited",
                    &event.event_id,
                    "event has no established-story reference",
                ));
            }
        }
    }

    findings
}

pub fn compare_to_established(
    history: &PeopleHistory,
    profile: &EstablishedStoryProfile,
) -> ComparisonReport {
    let findings = validate_history(history);
    let event_ids: BTreeSet<&str> = history
        .eras
        .iter()
        .flat_map(|era| era.events.iter().map(|event| event.event_id.as_str()))
        .collect();
    let person_ids: BTreeSet<&str> = history
        .eras
        .iter()
        .flat_map(|era| era.persons.iter().map(|person| person.person_id.as_str()))
        .collect();
    let story_paths = story_ref_paths(history);

    let missing_event_ids = missing(&profile.required_event_ids, &event_ids);
    let missing_person_ids = missing(&profile.required_person_ids, &person_ids);
    let missing_story_paths = profile
        .required_story_paths
        .iter()
        .filter(|path| !story_paths.contains(path.as_str()))
        .cloned()
        .collect::<Vec<_>>();
    let uncited_event_ids = history
        .eras
        .iter()
        .flat_map(|era| &era.events)
        .filter(|event| event.source_story_refs.is_empty())
        .map(|event| event.event_id.clone())
        .collect::<Vec<_>>();
    let uncited_person_ids = history
        .eras
        .iter()
        .flat_map(|era| &era.persons)
        .filter(|person| person.source_story_refs.is_empty())
        .map(|person| person.person_id.clone())
        .collect::<Vec<_>>();
    let external_framing_flags = external_framing_flags(history, profile);

    let has_error = findings
        .iter()
        .any(|finding| finding.severity == FindingSeverity::Error);
    let status = if has_error
        || !missing_event_ids.is_empty()
        || !missing_person_ids.is_empty()
        || !missing_story_paths.is_empty()
        || !uncited_event_ids.is_empty()
        || !uncited_person_ids.is_empty()
        || !external_framing_flags.is_empty()
    {
        ComparisonStatus::Hold
    } else {
        ComparisonStatus::Pass
    };

    ComparisonReport {
        profile_id: profile.profile_id.clone(),
        status,
        missing_event_ids,
        missing_person_ids,
        missing_story_paths,
        uncited_event_ids,
        uncited_person_ids,
        external_framing_flags,
        findings,
    }
}

fn require_non_empty(findings: &mut Vec<HistoryFinding>, code: &str, location: &str, value: &str) {
    if value.trim().is_empty() {
        findings.push(error(code, location, "required field is empty"));
    }
}

fn missing(required: &[String], actual: &BTreeSet<&str>) -> Vec<String> {
    required
        .iter()
        .filter(|id| !actual.contains(id.as_str()))
        .cloned()
        .collect()
}

fn story_ref_paths(history: &PeopleHistory) -> HashSet<&str> {
    let mut paths = HashSet::new();
    paths.extend(
        history
            .source_story_refs
            .iter()
            .map(|source| source.path.as_str()),
    );
    for era in &history.eras {
        paths.extend(
            era.source_story_refs
                .iter()
                .map(|source| source.path.as_str()),
        );
        for person in &era.persons {
            paths.extend(
                person
                    .source_story_refs
                    .iter()
                    .map(|source| source.path.as_str()),
            );
        }
        for event in &era.events {
            paths.extend(
                event
                    .source_story_refs
                    .iter()
                    .map(|source| source.path.as_str()),
            );
        }
    }
    paths
}

fn external_framing_flags(
    history: &PeopleHistory,
    profile: &EstablishedStoryProfile,
) -> Vec<String> {
    history
        .framing_notes
        .iter()
        .filter(|note| {
            let lower = note.to_lowercase();
            profile
                .forbidden_external_framings
                .iter()
                .any(|forbidden| lower.contains(&forbidden.to_lowercase()))
        })
        .cloned()
        .collect()
}

fn error(code: &str, location: &str, message: &str) -> HistoryFinding {
    HistoryFinding {
        severity: FindingSeverity::Error,
        code: code.to_string(),
        location: location.to_string(),
        message: message.to_string(),
    }
}

fn warning(code: &str, location: &str, message: &str) -> HistoryFinding {
    HistoryFinding {
        severity: FindingSeverity::Warning,
        code: code.to_string(),
        location: location.to_string(),
        message: message.to_string(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn story(path: &str) -> StoryRef {
        StoryRef {
            path: path.to_string(),
            anchor: None,
        }
    }

    fn sample_history() -> PeopleHistory {
        PeopleHistory {
            people_id: "mali-empire".to_string(),
            title: "Mali Empire people history".to_string(),
            worldview: "Mande political memory centered on kinship, obligation, gold roads, and learned cities.".to_string(),
            framing_notes: vec!["periodization remains internal to the Mali book".to_string()],
            source_story_refs: vec![story("regions/10-west-africa-sahel/mali-empire/eras/01-the-lions-time/chapter.md")],
            eras: vec![EraHistory {
                era_id: "01-the-lions-time".to_string(),
                title: "The Lion's Time".to_string(),
                source_story_refs: vec![story("regions/10-west-africa-sahel/mali-empire/eras/01-the-lions-time/chapter.md")],
                persons: vec![Person {
                    person_id: "sundiata".to_string(),
                    display_name: "Sundiata".to_string(),
                    role: "founding figure carried through epic and political memory".to_string(),
                    source_story_refs: vec![story("regions/10-west-africa-sahel/mali-empire/eras/01-the-lions-time/chapter.md")],
                }],
                events: vec![HistoryEvent {
                    event_id: "lion-kingship-formed".to_string(),
                    era_id: "01-the-lions-time".to_string(),
                    title: "Kingship forms around the lion story".to_string(),
                    event_kind: "political-memory".to_string(),
                    consequence: "The people history can compare later expansion against an established internal origin.".to_string(),
                    year_label: None,
                    actors: vec!["sundiata".to_string()],
                    places: vec!["Mande world".to_string()],
                    source_story_refs: vec![story("regions/10-west-africa-sahel/mali-empire/eras/01-the-lions-time/chapter.md")],
                }],
            }],
        }
    }

    #[test]
    fn valid_people_history_has_no_errors() {
        let findings = validate_history(&sample_history());

        assert!(findings
            .iter()
            .all(|finding| finding.severity != FindingSeverity::Error));
    }

    #[test]
    fn comparison_passes_when_required_story_elements_are_present() {
        let profile = EstablishedStoryProfile {
            profile_id: "mali-established-story".to_string(),
            required_event_ids: vec!["lion-kingship-formed".to_string()],
            required_person_ids: vec!["sundiata".to_string()],
            required_story_paths: vec![
                "regions/10-west-africa-sahel/mali-empire/eras/01-the-lions-time/chapter.md"
                    .to_string(),
            ],
            forbidden_external_framings: vec!["primitive".to_string()],
        };

        let report = compare_to_established(&sample_history(), &profile);

        assert_eq!(report.status, ComparisonStatus::Pass);
        assert!(report.missing_event_ids.is_empty());
        assert!(report.external_framing_flags.is_empty());
    }

    #[test]
    fn comparison_holds_when_established_story_requirements_are_missing() {
        let profile = EstablishedStoryProfile {
            profile_id: "mali-established-story".to_string(),
            required_event_ids: vec!["great-hajj".to_string()],
            required_person_ids: vec!["mansa-musa".to_string()],
            required_story_paths: vec!["missing.md".to_string()],
            forbidden_external_framings: vec!["primitive".to_string()],
        };

        let report = compare_to_established(&sample_history(), &profile);

        assert_eq!(report.status, ComparisonStatus::Hold);
        assert_eq!(report.missing_event_ids, vec!["great-hajj"]);
        assert_eq!(report.missing_person_ids, vec!["mansa-musa"]);
        assert_eq!(report.missing_story_paths, vec!["missing.md"]);
    }
}
