from pathlib import Path

from archive_manager.base import Card, Consultation
from core.logger import log_it


@log_it
def replace_card_from_archive() -> None:
    paths = []
    for template in Card.PATH_SIGNS:
        paths.extend(list(Path(Consultation.WORK_DIR).glob(template)))
    print(paths)


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
