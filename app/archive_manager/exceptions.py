class HeritageAttrNotExists(Exception):

    def __init__(self, attr: str):
        self.message = f"Необходимо задать {attr} в дочернем классе."
        super().__init__(self.message)


class OnlyFormatSupported(Exception):

    def __init__(self, supported: tuple[str]):
        supported_str = ", ".join(supported)
        self.message = f"Поддерживаются только фалы формата: {supported_str}."
        super().__init__(self.message)


class ImmutableFile(Exception):

    def __init__(self):
        self.message = "Файл не поддерживает изменение."
        super().__init__(self.message)


class InvalidString(Exception):

    def __init__(self, frame: tuple[str]):
        self.message = f"Некорректные данные в строке: {frame[0]} ..."
        super().__init__(self.message)


class StringNotExists(Exception):

    def __init__(self, frame: tuple[str]):
        self.message = f"Строка: {frame[0]} ... отсутствует в файле."
        super().__init__(self.message)
