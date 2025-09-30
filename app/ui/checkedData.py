from PyQt6.QtWidgets import (
    QCheckBox,
    QDialogButtonBox,
    QGridLayout,
    QGroupBox,
    QVBoxLayout,
    QWidget,
)

from app.ui.config import BACKGROUND_WIDGET_COLOR, CHECKBOXES_VERTICAL, CHECKBOXES_HORIZONTAL


class CheckboxGridWindow(QWidget):
    """Информация о пациенте."""
    def __init__(self, name: str, checkboxes: list[str]):
        super().__init__()

        self.name = name
        self.setStyleSheet(f"QLineEdit, QPlainTextEdit {{background-color: {BACKGROUND_WIDGET_COLOR}}}")
        mainLayout = QVBoxLayout()
        self.formGroupBox = QGroupBox(self.name)
        self.createForm(checkboxes)
        mainLayout.addWidget(self.formGroupBox)
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

    def createForm(self, checkboxes: list[str]):
        gridLayout = QGridLayout()
        iterator = iter(checkboxes)
        for h_idx in range(CHECKBOXES_VERTICAL):
            for w_idx in range(CHECKBOXES_HORIZONTAL):
                try:
                    checkbox = next(iterator)
                    gridLayout.addWidget(QCheckBox(checkbox), h_idx, w_idx)
                except StopIteration:
                    break

        self.formGroupBox.setLayout(gridLayout)
