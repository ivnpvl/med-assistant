import sys

from PyQt6.QtGui import QFont, QRegularExpressionValidator, QDoubleValidator
from PyQt6.QtWidgets import (QMainWindow, QLabel, QLineEdit, QFormLayout,
    QTextEdit, QGridLayout, QApplication, QWidget, QDialog, QVBoxLayout, QGroupBox,
    QDialogButtonBox, QPlainTextEdit, QHBoxLayout, QDateEdit, QCheckBox, QPushButton)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Назначение невролога")
        self.setFixedSize(1280, 640)
        self.setStyleSheet("background-color: #80C060; font-family: Courier; font-size: 12pt")
        self.mainWidget = QWidget()
        self.createMainWidget()
        self.setCentralWidget(self.mainWidget)

    def createMainWidget(self):
        self.mainWidget.setStyleSheet("QLineEdit, QPlainTextEdit {background-color: #90D070}")
        mainLayout = QVBoxLayout()
        self.formGroupBox = QGroupBox("Данные пациента")
        self.createForm()
        mainLayout.addWidget(self.formGroupBox)
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        mainLayout.addWidget(self.buttonBox)
        self.mainWidget.setLayout(mainLayout)

    def createForm(self):
        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(10)

        self.patientEdit = QLineEdit()
        self.patientEdit.setPlaceholderText("Фамилия Имя Отчество")
        self.formLayout.addRow("Пациент:", self.patientEdit)

        self.birthdateEdit = QLineEdit()
        self.birthdateEdit.setPlaceholderText("ДД.ММ.ГГГГ")
        self.formLayout.addRow("Дата рождения:", self.birthdateEdit)

        self.complaintEdit = QPlainTextEdit()
        self.complaintEdit.setPlaceholderText("Жалоб нет.")
        self.formLayout.addRow("Жалобы:", self.complaintEdit)

        self.headSizeEdit = QLineEdit()
        self.headSizeEdit.setPlaceholderText("34.5")
        self.headSizeEdit.setValidator(QDoubleValidator())
        self.formLayout.addRow("Голова, см:", self.headSizeEdit)

        self.chestSizeEdit = QLineEdit()
        self.chestSizeEdit.setPlaceholderText("34.5")
        self.chestSizeEdit.setValidator(QDoubleValidator())
        self.formLayout.addRow("Грудь, см:", self.chestSizeEdit)

        self.fountSizeEdit = QLineEdit()
        self.fountSizeEdit.setPlaceholderText("1.5")
        self.fountSizeEdit.setValidator(QDoubleValidator())
        self.formLayout.addRow("Большой родничок, мм:", self.fountSizeEdit)

        self.allergyEdit = QLineEdit()
        self.allergyEdit.setPlaceholderText("Наличие аллергических реакций отрицают.")
        self.formLayout.addRow("Аллергические реакции:", self.allergyEdit)

        self.addCardCheck = QPushButton("Завести новую амбулаторную карту")
        self.addCardCheck.setCheckable(True)
        self.addCardCheck.clicked.connect(self.addCardForm)
        self.formLayout.addRow(self.addCardCheck)

        # CARD_ELEMS = (
        #     "Пол:",
        #     "Населённый пункт:",
        #     "Адрес:",
        #     "Телефон:",
        # )
        self.formGroupBox.setLayout(self.formLayout)

    def addCardForm(self):
        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(10)

        self.p = QLineEdit()
        self.p.setPlaceholderText("Фамилия Имя Отчество")
        self.formLayout.addRow("Пациент:", self.p)



if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


#         # adding action when form is accepted
#         self.buttonBox.accepted.connect(self.getInfo)

#         # adding action when form is rejected
#         self.buttonBox.rejected.connect(self.reject)    

#     # get info method called when form is accepted
#     def getInfo(self):

#         # printing the form information
#         print("Person Name : {0}".format(self.nameLineEdit.text()))
#         print("Degree : {0}".format(self.degreeComboBox.currentText()))
#         print("Age : {0}".format(self.ageSpinBar.text()))

#         # closing the window
#         self.close()
