# Konfigurációs változók és beállítások
# src/config.py
from security import get_secret

class Config:
    VERIFY_TOKEN = get_secret("VERIFY_TOKEN")
    PAGE_ACCESS_TOKEN = get_secret("PAGE_ACCESS_TOKEN")
    GOOGLE_CLOUD_PROJECT = get_secret("GOOGLE_CLOUD_PROJECT")
    SHEET_NAME = "Shopping_List"  # Ez marad az .env-ből, ha szükséges
