import os
import sys
import json

class Config:
    # Detect base directory (works for both Python and PyInstaller .exe)
    if getattr(sys, 'frozen', False):
        BASE_DIR = os.path.dirname(sys.executable)
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            cfg = json.load(f)
    else:
        print(f"[WARNING] Config file not found: {CONFIG_FILE}")
        cfg = {}

    SQLALCHEMY_DATABASE_URI = cfg.get("SQLALCHEMY_DATABASE_URI", "sqlite:///default.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEMA_NAME = cfg.get("SCHEMA_NAME", "[default_schema]")
    BaseDirectoryPath = cfg.get("BaseDirectoryPath", "C:/DefaultPath")
    GOOGLE_TRANSLATOR_URL = cfg.get(
        "GOOGLE_TRANSLATOR_URL",
        "https://google.com/transliterate/indic"
    )
    PORT = cfg.get("PORT", 5000)   # default port = 5000

