use lucia_history_core::{
    compare_to_established, validate_history, EstablishedStoryProfile, PeopleHistory,
};
use std::{env, error::Error, fs, io};

fn main() -> Result<(), Box<dyn Error>> {
    let args = env::args().collect::<Vec<_>>();
    match args.as_slice() {
        [_, command, history_path] if command == "validate" => {
            let history = read_history(history_path)?;
            let findings = validate_history(&history);
            println!("{}", serde_json::to_string_pretty(&findings)?);
            if findings
                .iter()
                .any(|finding| finding.severity == lucia_history_core::FindingSeverity::Error)
            {
                std::process::exit(1);
            }
        }
        [_, command, history_path, profile_path] if command == "compare" => {
            let history = read_history(history_path)?;
            let profile = read_profile(profile_path)?;
            let report = compare_to_established(&history, &profile);
            println!("{}", serde_json::to_string_pretty(&report)?);
            if report.status == lucia_history_core::ComparisonStatus::Hold {
                std::process::exit(1);
            }
        }
        _ => {
            return Err(io::Error::new(
                io::ErrorKind::InvalidInput,
                "usage: lucia-history validate <people-history.json> | lucia-history compare <people-history.json> <established-profile.json>",
            )
            .into());
        }
    }
    Ok(())
}

fn read_history(path: &str) -> Result<PeopleHistory, Box<dyn Error>> {
    let text = fs::read_to_string(path)?;
    Ok(serde_json::from_str(&text)?)
}

fn read_profile(path: &str) -> Result<EstablishedStoryProfile, Box<dyn Error>> {
    let text = fs::read_to_string(path)?;
    Ok(serde_json::from_str(&text)?)
}
