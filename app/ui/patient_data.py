from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import (
    QDialogButtonBox,
    QGroupBox,
    QFormLayout,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ui.config import BACKGROUND_WIDGET_COLOR


class PatientDataWindow(QWidget):
    """Страница с информацией о пациенте."""
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"QLineEdit, QPlainTextEdit {{background-color: {BACKGROUND_WIDGET_COLOR}}}")
        mainLayout = QVBoxLayout()
        self.formGroupBox = QGroupBox("Данные пациента")
        self.createForm()
        mainLayout.addWidget(self.formGroupBox)
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

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
        print("Add card form")
        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(10)

        self.p = QLineEdit()
        self.p.setPlaceholderText("Фамилия Имя Отчество")
        self.formLayout.addRow("Пациент:", self.p)
