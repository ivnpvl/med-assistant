from docx import Document
from odf import text, teletype
from odf.opendocument import load
from pathlib import Path

from config import ARCHIVE_DIR, CARD_DIR, JSON_DIR
from templates import (
    CARD_STARTWITH_TEMPLATES,
    CONSULTATION_STARTWITH_TEMPLATES,
)


class File:

    def __init__(self, path: Path):
        self.path = path
        self.suffix = self.path.suffix
        self.document = self._get_document()
        self.paragraphs = self._get_paragraphs()

    def _get_document(self):
        if self.suffix == ".docx":
            return Document(self.path)
        if self.suffix == ".odt":
            return load(self.path)

    def _get_paragraphs(self):
        if self.suffix == ".docx":
            return self.document.paragraphs
        if self.suffix == ".odt":
            return self.document.getElementsByType(text.P)

    def get_text(self, paragraph) -> str:
        if self.suffix == ".docx":
            return paragraph.text
        if self.suffix == ".odt":
            return teletype.extractText(paragraph)

    def parse_startwith(self, template: str, edit=False):
        for paragraph in self.paragraphs:
            text = self.get_text(paragraph)
            if template in text:
                parsed = text.split(template)[1].split("\n")[0].strip()
                if edit:
                    return parsed, paragraph
                else:
                    return parsed

    def save(self):
        if self.suffix == ".docx":
            self.document.save(self.path)
        if self.suffix == ".odt":
            raise NotImplementedError("Файл .odt не поддерживает изменение.")


class Card(File):

    WORK_DIR = CARD_DIR
    JSON_PATH = JSON_DIR / "cards.json"
    STARTWITH_TEMPLATES = CARD_STARTWITH_TEMPLATES


class Consultation(File):

    WORK_DIR = ARCHIVE_DIR
    JSON_PATH = JSON_DIR / "consultations.json"
    STARTWITH_TEMPLATES = CONSULTATION_STARTWITH_TEMPLATES


class PercentageScale:

    def __init__(self, number: int, percent: int = 5):
        self.number = number
        self.percent = percent
        self.scale = self._get_percentage_scale()

    def _get_percentage_scale(self) -> dict:
        steps = [step for step in range(self.percent, 100, self.percent)]
        scale = {self.number * step // 100: step for step in steps}
        return scale

    def display(self, number):
        if number in self.scale:
            print(f"Обработано {self.scale[number]}% файлов.")
