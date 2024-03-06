class StringInvalidError(Exception):

    def __init__(self, frame: tuple[str]):
        self.message = f"Некорректные данные в строке: {frame[0]} ..."
        super().__init__(self.message)


class StringNotExistsError(Exception):

    def __init__(self, frame: tuple[str]):
        self.message = f"Строка: {frame[0]} ... отсутствует в файле."
        super().__init__(self.message)
