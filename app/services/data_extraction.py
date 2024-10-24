# app/services/data_extraction.py
import re

def extract_information(text: str) -> dict:
    coord_pattern = r"(\d{1,2}°\d{1,2}'[NS]),\s*(\d{1,3}°\d{1,2}'[EW])"
    issue_pattern = r"ISSUE:\s*(.*?)(?=\n|$)"

    coord_matches = re.findall(coord_pattern, text)
    issue_match = re.search(issue_pattern, text)

    return {
        "coordinates": coord_matches,
        "issue": issue_match.group(1).strip() if issue_match else "No specific issue"
    }
