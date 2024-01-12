from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent

ARCHIVE_DIR = BASE_DIR / "data/archive"

CARD_DIR = BASE_DIR / "data/card"

JSON_DIR = BASE_DIR / "data/json"

LOG_DIR = BASE_DIR / "data/journal"

STARTWITH_TEMPLATES_DOCX = {
    "date": "Дата:   ",
    "name": "Пациент:   ",
    "birthdate": "Дата рождения:   ",
}

STARTWITH_TEMPLATES_ODT = {
    "date": "Дата:",
    "name": "Пациент:",
    "birthdate": "Дата рождения:",
}

CONSULTATION_ATTRS = (
    "date",
    "surname",
    "name",
    "patronymic",
    "birthdate",
    "path",
)


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def database_URL(self):
        # DSN
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
