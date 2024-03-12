from datetime import date


def parse_number(data: str, max_digits: int) -> tuple[int, str]:
    number = ""
    record = False
    for i, char in enumerate(data, 1):
        if char.isdecimal():
            number += char
            if len(number) == max_digits:
                break
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
    if not data.replace(" ", ""):
        raise ValueError("Дата не указана.")
    day, data = parse_number(data, 2)
    month, data = parse_number(data, 2)
    year, data = parse_number(data, 4)
    current_date = date.today()
    year = normalize_year(year, current_date.year)
    normalized_date = date(year=year, month=month, day=day)
    if normalized_date > current_date or year < current_date.year - 80:
        raise ValueError("Неправильно указана дата.")
    return normalized_date

def normalize_name(data: str) -> str:
    if not data.replace(" ", ""):
        raise ValueError("Имя не указано.")
    data = "".join(filter(lambda char: char.isalpha or char.isspace, data))
    return " ".join(data.title().split())
