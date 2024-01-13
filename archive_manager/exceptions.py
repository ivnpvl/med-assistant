class AttrNotExistsError(Exception):

    def __init__(self, attr: str, message="Недостаточно данных, укажите {}."):
        self.message = message.format(attr)
        super().__init__(self.message)
