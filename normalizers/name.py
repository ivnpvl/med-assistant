def normalize_name(data: str) -> str:
    data = ''.join(filter(lambda char: char.isalpha or char.isspace, data))
    return ' '.join(data.title().split())
