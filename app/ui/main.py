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
    SELECT_BAR_WIDTH,
    SHEET_SIZE,
    TITLE,
)
from app.ui.checkedData import CheckboxGridWindow
from app.ui.patientData import PatientCardWindow, PatientDataWindow


class CentralWindow(QWidget):
    """Основное окно выбора страниц."""
    def __init__(self):
        super().__init__()
        self.selectBar = QListWidget()
        self.selectBar.setFixedWidth(SELECT_BAR_WIDTH)
        self.selectWindow = QStackedWidget()

        self.patientData = PatientDataWindow()
        self.selectBar.insertItem(0, self.patientData.name)
        self.selectWindow.addWidget(self.patientData)

        self.patientCard = PatientCardWindow()
        self.selectBar.insertItem(1, self.patientCard.name)
        self.selectWindow.addWidget(self.patientCard)

        self.baseStatus = CheckboxGridWindow()
        self.selectBar.insertItem(2, self.baseStatus.name)
        self.selectWindow.addWidget(self.baseStatus)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.selectBar)
        self.mainLayout.addWidget(self.selectWindow)
        self.setLayout(self.mainLayout)

        self.selectBar.currentRowChanged.connect(self.display)

    def display(self, idx):
        self.selectWindow.setCurrentIndex(idx)


class MainWindow(QMainWindow):
    """Основное окно приложения."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE)
        self.setFixedSize(*SHEET_SIZE)
        self.setStyleSheet(
            f"background-color: {BACKGROUND_SHEET_COLOR}; font-family: {FONT_FAMILY}; font-size: {FONT_SIZE}"
        )
        self.mainWidget = CentralWindow()
        self.setCentralWidget(self.mainWidget)


def init_ui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
