import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QListWidget,
    QMainWindow,
    QStackedWidget,
    QWidget,
)

from ui.config import (
    BACKGROUND_SHEET_COLOR,
    FONT_FAMILY,
    FONT_SIZE,
    SHEET_SIZE,
    TITLE,
)
from ui.patient_data import PatientDataWindow


class StackedWindow(QWidget):
    """Основное окно выбора страниц."""
    def __init__(self):
        super().__init__()
        self.leftList = QListWidget()
        self.leftList.insertItem(0, 'Данные пациента')
        self.leftList.insertItem(1, 'Personal')
        self.leftList.insertItem(2, 'Educational')

        self.patientData = PatientDataWindow()

        self.stack = QStackedWidget(parent=self)
        self.stack.addWidget(self.patientData)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftList)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)
        self.leftList.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()

    def display(self, idx):
        self.stack.setCurrentIndex(idx)


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


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
