from concurrent import futures
from pathlib import Path
from tqdm import tqdm

from archiver.base import Card, Consultation
from core.logger import log_it


@log_it
def replace_cards(paths: list[Path] = None) -> None:
    if not paths:
        paths = []
        for template in Card.PATH_SIGNS:
            paths.extend(Path(Consultation.WORK_DIR).glob(template))
    for path in paths:
        replace_card(path)


@log_it
def replace_card(path: Path) -> None:
    card = Card(path)
    card_data = card.extract_data()
    card_data["suffix"] = card.suffix
    path.replace(Card.WORK_DIR / Card.FILENAME_TEMPLATE.format(**card_data))


@log_it
def normalize_consultation_docx(path: Path) -> bool:
    consultation = Consultation(path)
    return consultation.normalize_docx()


@log_it
def normalize_consultations_docx() -> None:
    paths = list(Path(Consultation.WORK_DIR).glob("*.docx"))

    with futures.ProcessPoolExecutor() as executor:
        to_do = (executor.submit(
            normalize_consultation_docx, path) for path in paths)
        done_iter = futures.as_completed(to_do)
        edited_files = 0
        for future in tqdm(done_iter, ascii=True, total=len(paths)):
            edited_files += future.result()

    if edited_files:
        print(f"{edited_files} has been edit.")
