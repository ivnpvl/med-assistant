from PyQt6.QtWidgets import (
    QCheckBox,
    QDialogButtonBox,
    QGridLayout,
    QGroupBox,
    QVBoxLayout,
    QWidget,
)

from app.ui.checkboxes import base_status
from app.ui.config import BACKGROUND_WIDGET_COLOR, CHECKBOX_HEIGHT, CHECKBOX_WIDTH


class CheckboxGridWindow(QWidget):
    """Информация о пациенте."""
    def __init__(self, name: str = "Окно с опциями"):
        super().__init__()

        self.name = name
        self.setStyleSheet(f"QLineEdit, QPlainTextEdit {{background-color: {BACKGROUND_WIDGET_COLOR}}}")
        mainLayout = QVBoxLayout()
        self.formGroupBox = QGroupBox(self.name)
        self.createForm()
        mainLayout.addWidget(self.formGroupBox)
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

    def createForm(self):
        gridLayout = QGridLayout()
        checkBoxIterator = iter(base_status)
        for h_idx in range(CHECKBOX_HEIGHT):
            for w_idx in range(CHECKBOX_WIDTH):
                try:
                    checkBoxText = next(checkBoxIterator)
                    gridLayout.addWidget(QCheckBox(checkBoxText), h_idx, w_idx)
                except StopIteration:
                    break

        self.formGroupBox.setLayout(gridLayout)
