from docx import Document
from pathlib import Path

from logs.decorator import log_it
from normalizers.date import normalize_date
from settings import ARCHIVE_DIR


def get_percentage_scale(number, percent):
    steps = [step for step in range(percent, 100, percent)]
    return {number * step // 100: step for step in steps}


@log_it
def edit_docx_date(path, date_template="Дата рождения:   "):
    document = Document(path)
    for paragraph in document.paragraphs:
        if date_template in paragraph.text:
            date = paragraph.text.split(date_template)[1].split("\n")[0]
            normalized_date = normalize_date(date).strftime("%d.%m.%Y")
            if date != normalized_date:
                paragraph.text = paragraph.text.replace(date, normalized_date)
                document.save(path)
            break


def main():
    paths = list(map(str, Path(ARCHIVE_DIR).glob('*.docx')))
    status_bar = get_percentage_scale(len(paths), 5)
    for counter, path in enumerate(paths, 1):
        edit_docx_date(path)
        if counter in status_bar:
            print(f"Отредактировано {status_bar[counter]}% файлов.")


if __name__ == "__main__":
    main()
