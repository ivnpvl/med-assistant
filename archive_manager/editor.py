from docx import Document
from pathlib import Path

from config import ARCHIVE_DIR, STARTWITH_TEMPLATES
from logger.decorator import log_it
from normalizer import normalize_date, normalize_name
from util import PercentageScale


def edit_name_docx(document):
    name_template = STARTWITH_TEMPLATES["name"]
    for paragraph in document.paragraphs:
        if name_template in paragraph.text:
            name = paragraph.text.split(name_template)[1].split("\n")[0]
            normalized_name = normalize_name(name)
            if name != normalized_name:
                paragraph.text = paragraph.text.replace(name, normalized_name)
                return True
            return False
    return False


def edit_birthdate_docx(document):
    date_template = STARTWITH_TEMPLATES["birthdate"]
    for paragraph in document.paragraphs:
        if date_template in paragraph.text:
            date = paragraph.text.split(date_template)[1].split("\n")[0]
            normalized_date = normalize_date(date).strftime("%d.%m.%Y")
            if date != normalized_date:
                paragraph.text = paragraph.text.replace(date, normalized_date)
                return True
            return False
    return False


@log_it
def edit_and_save(path):
    document = Document(path)
    name_changed = edit_name_docx(document)
    birthdate_changed = edit_birthdate_docx(document)
    if name_changed or birthdate_changed:
        document.save(path)


def main():
    paths = list(map(str, Path(ARCHIVE_DIR).glob('*.docx')))
    status_bar = PercentageScale(len(paths), 10)
    for counter, path in enumerate(paths, 1):
        edit_and_save(path)
        status_bar.display(counter)


if __name__ == "__main__":
    main()
