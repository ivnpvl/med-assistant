class PercentageScale:

    def __init__(self, number, percent):
        self.number = number
        self.percent = percent
        self.scale = self.get_percentage_scale()

    def get_percentage_scale(self):
        steps = [step for step in range(self.percent, 100, self.percent)]
        scale = {self.number * step // 100: step for step in steps}
        return scale

    def display(self, number):
        if number in self.scale:
            print(f"Обработано {self.scale[number]}% файлов.")
