import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import SHEET_NAME
from security import get_secret
import json

def get_sheet():
    """Csatlakozik a Google Sheets-hez és visszaadja a bevásárlólista táblázatot."""
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    
    # A kulcsot közvetlenül a Secret Managerből töltjük be
    creds_json = json.loads(get_secret('GOOGLE_CREDENTIALS_SECRET_NAME'))  # A GOOGLE_CREDENTIALS_SECRET_NAME helyére írd be a tényleges titok nevét
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1  # A táblázat első lapjára csatlakozik

    return sheet

def add_item(item_name, quantity):
    """Hozzáad egy új tételt a bevásárlólistához."""
    sheet = get_sheet()
    sheet.append_row([item_name, quantity])
