import json
from pathlib import Path

from archive_manager.files import Card, Consultation
from informer import log_it, PercentageScale


@log_it
def parse_file(path: Path, Target: Card | Consultation) -> dict:
    document = Target(path)
    for attr, template in Target.STARTWITH_TEMPLATES.items():
        document.add_data(attr, template)
    return document.data


def parse_group(Target: Card | Consultation):
    folder = Target.WORK_DIR
    paths = list(path for path in Path(folder).iterdir() if path.suffix in (
        ".docx", ".odt"))
    status_bar = PercentageScale(len(paths))
    data = []
    for counter, path in enumerate(paths, 1):
        if record := parse_file(path, Target):
            data.append(record)
        status_bar.display(counter)
    with open(Target.JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    parse_group(Card)
