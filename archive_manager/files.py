from docx import Document
from odf import text, teletype
from odf.opendocument import load
from pathlib import Path
from typing import Callable

from config import ARCHIVE_DIR, CARD_DIR, JSON_DIR
from exceptions import StringInvalidError, StringNotExistsError
from normalizer import normalize_date, normalize_name
from templates import (
    CARD_PATH_TEMPLATES,
    CARD_STARTWITH_TEMPLATES,
    CARD_TITLE_ATTRS,
    CARD_TITLE_TEMPLATE,
    CONSULTATION_STARTWITH_TEMPLATES,
)


class File:

    def __init__(self, path: Path):
        self.path = path
        self.suffix = self.path.suffix
        self.document = self._get_document()
        self.paragraphs = self._get_paragraphs()
        self.data = {"path": str(path)}
        if self.suffix not in (".docx", ".odt"):
            raise NotImplementedError(
                "Поддерживаются только .docx или .odt расширения файлов."
            )

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

    @staticmethod
    def strip_bolders(text: str, left: str, right: str) -> str:
        return text.split(left)[1].split(right)[0].strip()

    def parse_startwith(self, startwith: str, endwith="\n") -> str:
        for paragraph in self.paragraphs:
            text = self.get_text(paragraph)
            if startwith in text:
                parsed = self.strip_bolders(text, startwith, endwith)
                if not parsed:
                    raise StringInvalidError(startwith)
                return parsed
        raise StringNotExistsError(startwith)

    def edit_startwith(self, startwith: str, normalize_func: Callable) -> bool:
        if self.suffix == ".odt":
            raise NotImplementedError("Файл .odt не поддерживает изменение.")
        for paragraph in self.paragraphs:
            text = paragraph.text
            if startwith in text:
                parsed = self.strip_bolders(text, startwith, endwith="\n")
                if not parsed:
                    raise StringInvalidError(startwith)
                normalized = normalize_func(parsed)
                if parsed != normalized:
                    paragraph.text = paragraph.text.replace(parsed, normalized)
                    return True
                return False
        raise StringNotExistsError(startwith)

    def add_data(self, attr: str, template: str) -> None:
        if attr == "address":
            parsed = self.parse_startwith(template, endwith=", тел.:")
        parsed = self.parse_startwith(template)
        if attr == "name":
            surname, name, patronymic = parsed.split()
            self.data["surname"] = surname
            self.data["name"] = name
            self.data["patronymic"] = patronymic
        else:
            self.data[attr] = parsed

    def save(self):
        if self.suffix == ".docx":
            self.document.save(self.path)
        if self.suffix == ".odt":
            raise NotImplementedError("Файл .odt не поддерживает изменение.")


class Card(File):

    WORK_DIR = CARD_DIR
    JSON_PATH = JSON_DIR / "cards.json"
    STARTWITH_TEMPLATES = CARD_STARTWITH_TEMPLATES
    PATH_TEMPLATES = CARD_PATH_TEMPLATES
    TITLE_TEMPLATE = CARD_TITLE_TEMPLATE
    TITLE_ATTRS = CARD_TITLE_ATTRS


class Consultation(File):

    WORK_DIR = ARCHIVE_DIR
    JSON_PATH = JSON_DIR / "consultations.json"
    STARTWITH_TEMPLATES = CONSULTATION_STARTWITH_TEMPLATES
    NORMALIZE_FUNCS = {
        "name": normalize_name,
        "birthdate": lambda data: normalize_date(data).strftime("%d.%m.%Y"),
    }
