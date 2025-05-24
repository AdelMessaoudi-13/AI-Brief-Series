import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_emails_from_sheet(sheet_name: str, worksheet_index: int = 0):
    """Fetch email addresses from Google Sheets (column 2 only)"""
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds_path = "service_account.json"
    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(credentials)

    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    data = sheet.col_values(2)[1:]  # column 2 = emails, skip header
    emails = sorted(set(email.strip() for email in data if email.strip()))
    return emails

def save_to_json(emails, output_path="subscribers.json"):
    """Save the email addresses into a JSON file in the expected format"""
    with open(output_path, "w") as f:
        json.dump({"subscribers": emails}, f, indent=2)
    print(f"✅ {len(emails)} email(s) saved to {output_path}")

if __name__ == "__main__":
    SHEET_NAME = "AI_Brief_Responses"  # exact name of the linked Google Sheet
    emails = get_emails_from_sheet(SHEET_NAME)
    save_to_json(emails)
