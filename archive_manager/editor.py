from pathlib import Path

from logger.decorator import log_it
from exceptions import AttrNotExistsError, AttrNotExistsInFileError
from util import Card, Consultation, PercentageScale


@log_it
def replace_cards_from_archive() -> None:
    paths = []
    for template in Card.PATH_TEMPLATES:
        paths.extend(list(Path(Consultation.WORK_DIR).glob(template)))
    for path in paths:
        document = Card(path)
        for attr in Card.TITLE_ATTRS:
            template = Card.STARTWITH_TEMPLATES.get(attr)
            parsed = document.parse_startwith(template)
        if not parsed:
            raise AttrNotExistsInFileError(attr, path)

        path.replace(Card.WORK_DIR / Card.TITLE_TEMPLATE.format(parsed))


@log_it
def normalize_docx(path: Path) -> None:
    document = Consultation(path)
    is_changed = False
    for attr, normalize_func in Consultation.NORMALIZE_FUNCS.items():
        template = Consultation.STARTWITH_TEMPLATES.get(attr)
        try:
            edit = document.edit_startwith(template, normalize_func)
        except Exception:
            raise AttrNotExistsError(attr)
        is_changed = is_changed | edit
    if is_changed:
        document.save()


def main():
    replace_cards_from_archive()


if __name__ == "__main__":
    main()
