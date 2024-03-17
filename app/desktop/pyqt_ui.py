
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QMainWindow, QLabel, QLineEdit, QFormLayout,
    QTextEdit, QGridLayout, QApplication, QWidget, QDialog, QVBoxLayout, QGroupBox, 
    QDialogButtonBox)


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Назначение невролога")
        self.setMinimumSize(1280, 640)
        self.setStyleSheet("background-color: #80C060; font-family: Courier; font-size: 14pt")
        # QLineEdit, QTextEdit{background-color: #A0E080}
        self.setFont(QFont("Arial", 40))
        self.initUI()
        self.show()

    def initUI(self):

        mainLayout = QVBoxLayout()
        self.formGroupBox = QGroupBox("Form 1")
        self.createForm()
        mainLayout.addWidget(self.formGroupBox)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)


    def createForm(self):
        layout = QFormLayout()
        layout.setSpacing(10)
        patient_edit = QLineEdit()
        layout.addRow("Пациент:", patient_edit)
        birthdate_edit = QLineEdit()
        layout.addRow("Дата рождения:", birthdate_edit)
        complaint_edit = QTextEdit()
        # complaint_edit.setFixedHeight(3)
        layout.addRow("Жалобы:", complaint_edit)

        #     (QLabel("Жалобы:"), QTextEdit().setFixedHeight(3)),
        #     (QLabel("Голова, см:"), QLineEdit()),
        #     (QLabel("Грудь, см:"), QLineEdit()),
        #     (QLabel("Большой родничок, мм:"), QLineEdit()),
        #     (QLabel("Аллергические реакции:"), QLineEdit()),
        # )

        # CARD_ELEMS = (
        #     "Пол:",
        #     "Населённый пункт:",
        #     "Адрес:",
        #     "Телефон:",
        # )
        self.formGroupBox.setLayout(layout)


if __name__ == "__main__":

    app = QApplication([])
    window = Window()
    app.exec()


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
