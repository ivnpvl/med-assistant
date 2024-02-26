import json
from concurrent import futures
from pathlib import Path
from tqdm import tqdm

from files import Card, Consultation
from informer import log_it


@log_it
def parse_file(path: Path, klass: Card | Consultation) -> dict:
    document = klass(path)
    for attr, template in klass.STARTWITH_TEMPLATES.items():
        document.add_data(attr, template)
    return document.data


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


if __name__ == "__main__":
    parse_group(Card)
