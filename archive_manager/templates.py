CARD_FILENAME_TEMPLATE = "Карта № {number} {surname} {name}{suffix}"

CARD_FILENAME_ATTRS = ("number", "name")

CARD_PARSE_RANGE = {
    "number": ("АМБУЛАТОРНЫХ УСЛОВИЯХ №",),
    "name": ("Фамилия, имя, отчество:",),
    "gender": ("Пол:",),
    "birthdate": ("Дата рождения:",),
    "address": ("Место регистрации:", "тел.:"),
    "phone": ("тел.:",),
}

CARD_PATH_SIGNS = ("*карта*", "*карточка*")

CONSULTATION_PARSE_RANGE = {
    "date": ("Дата:",),
    "name": ("Пациент:",),
    "birthdate": ("Дата рождения:",),
}
