
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QMainWindow, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QWidget)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Назначение невролога")
        self.setMinimumSize(1280, 640)
        self.setStyleSheet("background-color: #80C060; font-family: Courier; font-size: 14pt")
        self.setFont(QFont("Arial", 40))
        self.initUI()
        self.show()

    def initUI(self):

        widget = QWidget()

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        widget.setLayout(grid)
        widget.setStyleSheet("QLineEdit, QTextEdit {background-color: #A0E080}")
        self.setCentralWidget(widget)



if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec()
