from pathlib import Path

from config import ARCHIVE_DIR
from logger.decorator import log_it
from normalizer import normalize_date, normalize_name
from util import File, PercentageScale


@log_it
def edit_name_birthdate_docx(path: Path) -> None:
    attrs = ("name", "birthdate")
    document = File(path)
    is_changed = False
    for attr in attrs:
        template = document.startwith_templates.get(attr)
        for paragraph in document.paragraphs:
            text = paragraph.text
            if template in text:
                parsed = text.split(template)[1].split("\n")[0].strip()
                if attr == "name":
                    normalized = normalize_name(parsed)
                elif attr == "birthdate":
                    normalized = normalize_date(parsed).strftime("%d.%m.%Y")
                if parsed != normalized:
                    paragraph.text = text.replace(parsed, normalized)
                    is_changed = True
                    break
    if is_changed:
        document.save()


def main():
    paths = list(Path(ARCHIVE_DIR).glob('*.docx'))
    status_bar = PercentageScale(len(paths), 5)
    print(str(paths[200]))
    edit_name_birthdate_docx(paths[200])


if __name__ == "__main__":
    main()
