import json
from pathlib import Path

from logger.decorator import log_it
from exceptions import AttrNotExistsError
from util import Card, Consultation, PercentageScale


@log_it
def parse_file(path: Path, target: Card | Consultation) -> dict:
    document = target(path)
    data = {}
    for attr, template in document.STARTWITH_TEMPLATES.items():
        parsed = document.parse_startwith(template)
        if not parsed:
            raise AttrNotExistsError(attr)
        if attr == "name":
            data["surname"], data["name"], data["patronymic"] = \
                parsed.split()
        else:
            data[attr] = parsed
    return data


def parse_group(target: Card | Consultation, add_path=False):
    dir = target.WORK_DIR
    paths = list(path for path in Path(dir).iterdir() if path.suffix in (
        ".docx", ".odt"))
    status_bar = PercentageScale(len(paths))
    data = []
    for counter, path in enumerate(paths, 1):
        if record := parse_file(path, target):
            if add_path:
                record["path"] = str(path)
            data.append(record)
        status_bar.display(counter)
    with open(target.JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    parse_group(Card)
