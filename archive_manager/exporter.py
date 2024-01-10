import json
from docx import Document
from pathlib import Path

from config import ARCHIVE_DIR, JSON_DIR, STARTWITH_TEMPLATES
from logger.decorator import log_it
from util import PercentageScale


@log_it
def parse_docx(path):
    document = Document(path)
    data = {}
    for attr, template in STARTWITH_TEMPLATES.items():
        for paragraph in document.paragraphs:
            if template in paragraph.text:
                parsed = paragraph.text.split(template)[1].split("\n")[0]
                if attr == "name":
                    data["surname"], data["name"], data["patronymic"] = parsed.split()
                else:
                    data[attr] = parsed
                break
    return data


def main():
    paths = list(map(str, Path(ARCHIVE_DIR).glob('*.docx')))[:100]
    status_bar = PercentageScale(len(paths), 10)
    with open(JSON_DIR / "consultations.json", "w", encoding="utf-8") as file:
        json.dump([{"ssd": "asd", "ssad": "asd"}], file, ensure_ascii=False)
        for counter, path in enumerate(paths, 1):
            data = parse_docx(path)
            if data:
                json.dump(data, file, ensure_ascii=False)
            status_bar.display(counter)


if __name__ == "__main__":
    main()
