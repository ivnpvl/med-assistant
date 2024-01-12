from pathlib import Path

from config import ARCHIVE_DIR, CARD_DIR
from logger.decorator import log_it
from normalizer import normalize_date, normalize_name
from util import File, PercentageScale, parse_by_startwith


@log_it
def replace_cards_from_archive() -> None:
    card_templates = ("*карта*", "*карточка*")
    startwith_template = "АМБУЛАТОРНЫХ УСЛОВИЯХ №"
    title_template = "Амбулаторная карта № {}.odt"
    paths = []
    for card_template in card_templates:
        paths.extend(list(Path(ARCHIVE_DIR).glob(card_template)))
    for path in paths:
        document = File(path)
        for paragraph in document.paragraphs:
            text = document.get_text(paragraph)
            if startwith_template in text:
                parsed = parse_by_startwith(text, startwith_template)
                if not parsed:
                    raise ValueError(f"Не указан номер карты {path}.")
                path.replace(CARD_DIR / title_template.format(parsed))
                break
        else:
            raise ValueError("Некорректный формат карты.")


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
                parsed = parse_by_startwith(text, template)
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
    replace_cards_from_archive()


if __name__ == "__main__":
    main()
