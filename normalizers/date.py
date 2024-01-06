from datetime import date


def parse_number(data: str) -> tuple[int, str]:
    number = ""
    record = False
    for i, char in enumerate(data):
        if char.isdecimal():
            number += char
            record = True
        elif record:
            break
    return int(number), data[i:]


def normalize_year(year: int, current_year: int) -> int:
    if year < 100:
        if year + 2000 <= current_year:
            return year + 2000
        return year + 1900
    return year


def normalize_date(data: str) -> date:
    day, data = parse_number(data)
    month, data = parse_number(data)
    year, data = parse_number(data)
    current_date = date.today()
    year = normalize_year(year, current_date.year)
    normalized_date = date(year=year, month=month, day=day)
    if normalized_date > current_date or year < current_date.year - 80:
        raise ValueError("Неправильно указана дата.")
    return normalized_date
