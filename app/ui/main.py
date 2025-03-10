import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QListWidget,
    QMainWindow,
    QStackedWidget,
    QWidget,
)

from app.ui.config import (
    BACKGROUND_SHEET_COLOR,
    FONT_FAMILY,
    FONT_SIZE,
    SHEET_SIZE,
    TITLE,
)
from app.ui.patientData import PatientCardWindow, PatientDataWindow


class StackedWindow(QWidget):
    """Основное окно выбора страниц."""
    def __init__(self):
        super().__init__()
        self.windowTag = QListWidget()
        self.windowTag.insertItem(0, 'Данные пациента')
        self.windowTag.insertItem(1, 'Амбулаторная карта')

        self.patientData = PatientDataWindow()
        self.patientCard = PatientCardWindow()

        self.windowStack = QStackedWidget(parent=self)
        self.windowStack.addWidget(self.patientData)
        self.windowStack.addWidget(self.patientCard)

        hBoxLayout = QHBoxLayout(self)
        hBoxLayout.addWidget(self.windowTag, stretch=1)
        hBoxLayout.addWidget(self.windowStack, stretch=5)
        self.setLayout(hBoxLayout)
        self.windowTag.currentRowChanged.connect(self.display)
        self.show()

    def display(self, idx):
        self.windowStack.setCurrentIndex(idx)


class MainWindow(QMainWindow):
    """Основное окно приложения."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE)
        self.setFixedSize(*SHEET_SIZE)
        self.setStyleSheet(
            f"background-color: {BACKGROUND_SHEET_COLOR}; font-family: {FONT_FAMILY}; font-size: {FONT_SIZE}"
        )
        self.mainWidget = StackedWindow()
        self.setCentralWidget(self.mainWidget)


def init_ui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
