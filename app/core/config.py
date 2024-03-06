from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"

ARCHIVE_DIR = DATA_DIR / "archive"

CARD_DIR = DATA_DIR / "card"

JSON_DIR = DATA_DIR / "json"

LOG_DIR = DATA_DIR / "journal"
