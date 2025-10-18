from PyQt6.QtWidgets import QCheckBox, QGridLayout, QWidget

from app.ui.config import CHECKBOXES_VERTICAL, CHECKBOXES_HORIZONTAL, WINDOW_STYLE_SHEET


class CheckboxGridWindow(QWidget):
    """Информация о пациенте."""
    def __init__(self, name: str, checkbox_names: list[str]):
        super().__init__()

        self.name = name
        self.setStyleSheet(WINDOW_STYLE_SHEET)

        self.gridCheckboxLayout = QGridLayout()
        iterator = iter(checkbox_names)
        for h_idx in range(CHECKBOXES_VERTICAL):
            for w_idx in range(CHECKBOXES_HORIZONTAL):
                try:
                    text = next(iterator)
                    checkbox = QCheckBox(text)
                    self.gridCheckboxLayout.addWidget(checkbox, h_idx, w_idx)
                except StopIteration:
                    break

        self.setLayout(self.gridCheckboxLayout)

    def extract(self) -> list[str]:
        data = []
        for checkbox in self.gridCheckboxLayout.children():
            checkbox: QCheckBox
            if checkbox.isChecked():
                data.append(checkbox.text())

        return data
