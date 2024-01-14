from pathlib import Path


class AttrNotExistsError(Exception):

    def __init__(self, attr: str, message="Недостаточно данных, укажите {}."):
        self.message = message.format(attr)
        super().__init__(self.message)


class AttrNotExistsInFileError(Exception):

    def __init__(
        self,
        attr: str,
        path: Path,
        message="Недостаточно данных в файле {}, укажите {}."
    ):
        self.message = message.format(str(path), attr)
        super().__init__(self.message)
