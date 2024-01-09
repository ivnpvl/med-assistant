def normalize_name(data: str) -> str:
    if not data.replace(" ", ""):
        raise ValueError("Имя не указано.")
    data = ''.join(filter(lambda char: char.isalpha or char.isspace, data))
    return ' '.join(data.title().split())
