from concurrent import futures
import json
from pathlib import Path
from tqdm import tqdm

from files import Card, Consultation
from informer import log_it


@log_it
def parse_file(path: Path, Target: Card | Consultation) -> dict:
    document = Target(path)
    for attr, template in Target.STARTWITH_TEMPLATES.items():
        document.add_data(attr, template)
    return document.data


def parse_group(Target: Card | Consultation):
    # executor = futures.ProcessPoolExecutor()
    # actual_workers = executor._max_workers
    # print(f"{actual_workers=}")
    folder = Target.WORK_DIR
    paths = list(path for path in Path(folder).iterdir() if path.suffix in (
        ".docx", ".odt"))
    data = []
    for path in tqdm(paths):
        if record := parse_file(path, Target):
            data.append(record)
    with open(Target.JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    parse_group(Card)
