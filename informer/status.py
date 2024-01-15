class PercentageScale:

    def __init__(self, number: int, percent: int = 5):
        self.number = number
        self.percent = percent
        self.scale = self._get_percentage_scale()

    def _get_percentage_scale(self) -> dict:
        steps = [step for step in range(self.percent, 100, self.percent)]
        scale = {self.number * step // 100: step for step in steps}
        return scale

    def display(self, number):
        if number in self.scale:
            print(f"Обработано {self.scale[number]}% файлов.")
