from docx import Document
from pathlib import Path

from normalizers.date import normalize_date
from settings import ARCHIVE_DIR


def get_percentage_scale(number, percent):
    steps = [percent * n for n in range(1, 100 // percent + 1)]
    return {number * step // 100: step for step in steps}


paths = list(map(str, Path(ARCHIVE_DIR).glob('*.docx')))
status_bar = get_percentage_scale(len(paths), 5)
date_template = "Дата рождения:   "

for counter, path in enumerate(paths, 1):
    document = Document(path)
    for paragraph in document.paragraphs:
        if date_template in paragraph.text:
            date = paragraph.text.split(date_template)[1].split("\n")[0]
            normalized_date = normalize_date(date).strftime("%d.%m.%Y")
            paragraph.text = paragraph.text.replace(date, normalized_date)
            break
    document.save(path)
    if counter in status_bar:
        print("Отредактировано {status_bar[counter]}% файлов.")
