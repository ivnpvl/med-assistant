import json
from pathlib import Path

from config import ARCHIVE_DIR, JSON_DIR
from logger.decorator import log_it
from .exceptions import AttrNotExistsError
from .templates import CONSULTATION_ATTRS
from .util import File, PercentageScale


@log_it
def parse_consultation(path: Path) -> dict:
    document = File(path)
    data = {}
    for attr, template in document.startwith_templates.items():
        parsed = document.parse_startwith(template)
        if not parsed:
            raise AttrNotExistsError(attr)
        if attr == "name":
            data["surname"], data["name"], data["patronymic"] = \
                parsed.split()
        else:
            data[attr] = parsed
    data["path"] = str(path)
    if not all(attr in data for attr in CONSULTATION_ATTRS):
        raise ValueError("Недостаточно данных о пациенте.")
    return data


def main():
    paths = list(
        path for path in Path(ARCHIVE_DIR).iterdir() if path.suffix in (
            ".docx",
            ".odt",
        )
    )
    status_bar = PercentageScale(len(paths), 5)
    data = []
    for counter, path in enumerate(paths, 1):
        if row := parse_consultation(path):
            data.append(row)
        status_bar.display(counter)
    with open(JSON_DIR / "consultations.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
