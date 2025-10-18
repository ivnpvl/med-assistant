from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import (
    QButtonGroup,
    QFormLayout,
    QLineEdit,
    QPlainTextEdit,
    QRadioButton,
    QHBoxLayout,
    QWidget,
)

from app.ui.config import WINDOW_STYLE_SHEET


class PatientDataWindow(QWidget):
    def __init__(self, name: str):
        super().__init__()

        self.name = name
        self.setStyleSheet(WINDOW_STYLE_SHEET)

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

        self.setLayout(self.formLayout)


class PatientCardWindow(QWidget):
    def __init__(self, name: str):
        super().__init__()

        self.name = name
        self.setStyleSheet(WINDOW_STYLE_SHEET)

        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(10)

        self.sexMaleButton = QRadioButton("мужской")
        self.sexFemaleButton = QRadioButton("женский")
        self.sexButtonLayout = QHBoxLayout()
        self.sexButtonLayout.addWidget(self.sexMaleButton)
        self.sexButtonLayout.addWidget(self.sexFemaleButton)
        self.sexButtonLayout.addStretch()
        self.formLayout.addRow("Пол:", self.sexButtonLayout)

        self.sexButtonGroup = QButtonGroup()
        self.sexButtonGroup.addButton(self.sexMaleButton)
        self.sexButtonGroup.addButton(self.sexFemaleButton)

        self.settlementEdit = QLineEdit()
        self.settlementEdit.setPlaceholderText("Пензенская обл., г. Пенза")
        self.formLayout.addRow("Населённый пункт:", self.settlementEdit)

        self.addressEdit = QLineEdit()
        self.addressEdit.setPlaceholderText("ул. Пушкина, 15")
        self.formLayout.addRow("Адрес:", self.addressEdit)

        self.phoneNumberEdit = QLineEdit()
        self.phoneNumberEdit.setPlaceholderText("+7(987)654-32-10")
        self.formLayout.addRow("Телефон:", self.phoneNumberEdit)

        self.setLayout(self.formLayout)
