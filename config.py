from pathlib import Path
# from pydantic_settings import BaseSettings, SettingsConfigDict

def create_dir(parent: Path, name: str):
    new_dir = parent / name
    new_dir.mkdir(exist_ok=True)
    return new_dir


BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = create_dir(BASE_DIR, "data")

ARCHIVE_DIR = create_dir(DATA_DIR, "archive")

CARD_DIR = create_dir(DATA_DIR, "card")

JSON_DIR = create_dir(DATA_DIR, "json")

LOG_DIR = create_dir(DATA_DIR, "journal")


# class Settings(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASS: str
#     DB_NAME: str

#     @property
#     def database_URL(self):
#         # DSN
#         return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

#     model_config = SettingsConfigDict(env_file=".env")


# settings = Settings()
