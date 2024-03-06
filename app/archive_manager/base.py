from docx import Document
from odf import text, teletype
from odf.opendocument import load
from pathlib import Path
from typing import Callable

from archive_manager import exceptions, templates
from archive_manager.normalizer import normalize_date, normalize_name
from core.config import ARCHIVE_DIR, CARD_DIR, JSON_DIR


class ArchiveFile:

    EXTENSIONS = (".docx", ".odt")

    def __init__(self, path: Path) -> None:
        self.path = path
        self.suffix = path.suffix
        if self.suffix not in self.__class__.EXTENSIONS:
            raise exceptions.OnlyFormatSupported(self.__class__.EXTENSIONS)
        self.document = self._load_document()
        self.paragraphs = self._get_paragraphs()

    def _load_document(self):
        if self.suffix == ".docx":
            return Document(self.path)
        if self.suffix == ".odt":
            return load(self.path)

    def _get_paragraphs(self):
        if self.suffix == ".docx":
            return self.document.paragraphs
        if self.suffix == ".odt":
            return self.document.getElementsByType(text.P)

    def extract_text(self, paragraph) -> str:
        if self.suffix == ".docx":
            return paragraph.text
        if self.suffix == ".odt":
            return teletype.extractText(paragraph)

    @staticmethod
    def strip_bolders(text: str, startwith: str, endwith: str = "\n") -> str:
        return text.split(startwith)[1].split(endwith)[0].strip()

    def parse(self, frame: tuple[str]) -> str:
        for paragraph in self.paragraphs:
            text = self.extract_text(paragraph)
            if frame[0] in text:
                parsed = self.strip_bolders(text, *frame)
                if not parsed:
                    raise exceptions.InvalidString(frame)
                return parsed
        raise exceptions.StringNotExists(frame)

    def extract_data(self) -> dict:
        parse_attr = "PARSE_FRAMES"
        if not hasattr(self, parse_attr):
            raise exceptions.HeritageAttrNotExists(parse_attr)
        data = {}
        for attr, frame in self.PARSE_FRAMES.items():
            parsed = self.parse(frame)
            if attr == "fullname":
                try:
                    surname, name, patronymic = parsed.split()
                except ValueError:
                    raise exceptions.InvalidString(frame)
                data["surname"] = surname
                data["name"] = name
                data["patronymic"] = patronymic
            else:
                data[attr] = parsed
        return data


class Card(ArchiveFile):

    WORK_DIR = CARD_DIR
    JSON_PATH = JSON_DIR / "cards.json"
    FILENAME_TEMPLATE = templates.CARD_FILENAME_TEMPLATE
    PARSE_FRAMES = templates.CARD_PARSE_FRAMES
    PATH_SIGNS = templates.CARD_PATH_SIGNS


class Consultation(ArchiveFile):

    WORK_DIR = ARCHIVE_DIR
    JSON_PATH = JSON_DIR / "consultations.json"
    NORMALIZE_FUNCS = {
        "fullname": normalize_name,
        "birthdate": lambda data: normalize_date(data).strftime("%d.%m.%Y"),
    }
    PARSE_FRAMES = templates.CONSULTATION_PARSE_FRAMES

    def normalize_docx(self) -> bool:
        if self.suffix != ".docx":
            raise exceptions.ImmutableFile()
        is_changed = False
        for attr, edit_func in self.__class__.NORMALIZE_FUNCS.items():
            frame = self.__class__.PARSE_FRAMES.get(attr)
            edit = self._parse_and_edit_docx(frame, edit_func)
            is_changed = is_changed | edit
        if is_changed:
            self.document.save(self.path)
        return is_changed

    def _parse_and_edit_docx(
        self,
        frame: tuple[str],
        edit_func: Callable,
    ) -> bool:
        for paragraph in self.paragraphs:
            text = paragraph.text
            if frame[0] in text:
                parsed = self.strip_bolders(text, *frame)
                if not parsed:
                    raise exceptions.InvalidString(frame)
                edited = edit_func(parsed)
                if parsed != edited:
                    paragraph.text = paragraph.text.replace(parsed, edited)
                    return True
                return False
        raise exceptions.StringNotExists(frame)
