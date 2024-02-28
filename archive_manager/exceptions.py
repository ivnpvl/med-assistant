class StringInvalidError(Exception):

    def __init__(self, startwith: str):
        self.message = f"Некорректные данные в строке: {startwith} ..."
        super().__init__(self.message)


class StringNotExistsError(Exception):

    def __init__(self, startwith: str):
        self.message = f"Строка: {startwith} ... отсутствует в файле."
        super().__init__(self.message)
