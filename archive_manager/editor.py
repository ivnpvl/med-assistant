from pathlib import Path

from files import Card, Consultation
from informer import log_it, PercentageScale


# @log_it
# def replace_cards_from_archive() -> None:
#     paths = []
#     for template in Card.PATH_TEMPLATES:
#         paths.extend(list(Path(Consultation.WORK_DIR).glob(template)))
#     for path in paths:


@log_it
def replace_card(path: Path) -> None:
    document = Card(path)
    for attr in Card.TITLE_ATTRS:
        template = Card.STARTWITH_TEMPLATES.get(attr)
        document.add_data(attr, template)
    document.data["suffix"] = document.suffix
    path.replace(Card.WORK_DIR / Card.TITLE_TEMPLATE.format(**document.data))
    print(path)


@log_it
def normalize_docx(path: Path) -> None:
    document = Consultation(path)
    is_changed = False
    for attr, normalize_func in Consultation.NORMALIZE_FUNCS.items():
        template = Consultation.STARTWITH_TEMPLATES.get(attr)
        edit = document.edit_startwith(template, normalize_func)
        is_changed = is_changed | edit
    if is_changed:
        document.save()


def main():
    pass


if __name__ == "__main__":
    main()
