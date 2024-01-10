import json
from docx import Document
from odf import text, teletype
from odf.opendocument import load
from pathlib import Path

from config import ARCHIVE_DIR, JSON_DIR, STARTWITH_TEMPLATES_DOCX, STARTWITH_TEMPLATES_ODT
from logger.decorator import log_it
from util import PercentageScale


@log_it
def parse_docx(path):
    document = Document(path)
    data = {}
    for attr, template in STARTWITH_TEMPLATES_DOCX.items():
        for paragraph in document.paragraphs:
            if template in paragraph.text:
                parsed = paragraph.text.split(template)[1].split("\n")[0]
                if attr == "name":
                    data["surname"], data["name"], data["patronymic"] = parsed.split()
                else:
                    data[attr] = parsed
                break
    data["path"] = path
    return data


@log_it
def parse_odt(path):
    document = load(path)
    data = {}
    for attr, template in STARTWITH_TEMPLATES_ODT.items():
        for paragraph in document.getElementsByType(text.P):
            paragraph_text = teletype.extractText(paragraph)
            if template in paragraph_text:
                parsed = paragraph_text.split(template)[1].split("\n")[0]
                if attr == "name":
                    data["surname"], data["name"], data["patronymic"] = parsed.split()
                else:
                    data[attr] = parsed.strip()
                break
    data["path"] = path
    return data


def main():
    paths = list(map(str, Path(ARCHIVE_DIR).glob('*.docx')))
    status_bar = PercentageScale(len(paths), 10)
    data = []
    print("Начата обработка документов .docx")
    for counter, path in enumerate(paths, 1):
        if row := parse_docx(path):
            data.append(row)
        status_bar.display(counter)

    paths = list(map(str, Path(ARCHIVE_DIR).glob('*.odt')))
    status_bar = PercentageScale(len(paths), 10)
    print("Начата обработка документов .odt")
    for counter_odt, path in enumerate(paths, 1):
        if row := parse_odt(path):
            data.append(row)
        status_bar.display(counter_odt)

    with open(JSON_DIR / "consultations.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
