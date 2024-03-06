import json
from concurrent import futures
from pathlib import Path
from tqdm import tqdm

from archive_manager.base import Card, Consultation
from app.core.logger import log_it


@log_it
def parse_file(path: Path, klass: Card | Consultation) -> dict:
    document = klass(path)
    return document.extract_data()


def parse_group(klass: Card | Consultation):
    folder = klass.WORK_DIR
    paths = [path for path in Path(folder).iterdir() if path.suffix in (
        ".docx", ".odt")]
    with futures.ProcessPoolExecutor() as executor:
        to_do = (executor.submit(parse_file, path, klass) for path in paths)
        done_iter = futures.as_completed(to_do)
        data = []
        for future in tqdm(done_iter, ascii=True, total=len(paths)):
            if record := future.result():
                data.append(record)
    with open(klass.JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
