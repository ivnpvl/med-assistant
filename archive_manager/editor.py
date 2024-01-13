from pathlib import Path

from config import ARCHIVE_DIR, CARD_DIR
from logger.decorator import log_it
from normalizer import normalize_date, normalize_name
from exceptions import AttrNotExistsError
from templates import CARD_FILE_TEMPLATES
from util import Card, Consultation, PercentageScale


@log_it
def replace_cards_from_archive() -> None:
    card_templates = CARD_FILE_TEMPLATES
    startwith_template = "АМБУЛАТОРНЫХ УСЛОВИЯХ №"
    title_template = "Амбулаторная карта № {}.odt"
    paths = []
    for card_template in card_templates:
        paths.extend(list(Path(ARCHIVE_DIR).glob(card_template)))
    for path in paths:
        document = File(path)
        parsed = document.parse_startwith(startwith_template)
        if not parsed:
            raise ValueError(f"Не указан номер карты {path}.")
        path.replace(CARD_DIR / title_template.format(parsed))


@log_it
def edit_name_birthdate_docx(path: Path) -> None:
    attrs = ("name", "birthdate")
    document = File(path)
    is_changed = False
    for attr in attrs:
        template = document.startwith_templates.get(attr)
        parsed, paragraph = document.parse_startwith(template, edit=True)
        if not parsed:
            raise AttrNotExistsError(attr)
        if attr == "name":
            normalized = normalize_name(parsed)
        elif attr == "birthdate":
            normalized = normalize_date(parsed).strftime("%d.%m.%Y")
        if parsed != normalized:
            paragraph.text = paragraph.text.replace(parsed, normalized)
            is_changed = True
    if is_changed:
        document.save()


def main():
    replace_cards_from_archive()


if __name__ == "__main__":
    main()
