CARD_FILENAME_TEMPLATE = "Карта № {number} {surname} {name}{suffix}"

CARD_FILENAME_ATTRS = ("number", "name")

CARD_PARSE_FRAMES = {
    "number": ("АМБУЛАТОРНЫХ УСЛОВИЯХ №",),
    "fullname": ("Фамилия, имя, отчество:",),
    "gender": ("Пол:",),
    "birthdate": ("Дата рождения:",),
    "address": ("Место регистрации:", "тел.:"),
    "phone": ("тел.:",),
}

CARD_PATH_SIGNS = ("*карта*", "*карточка*")

CONSULTATION_PARSE_FRAMES = {
    "date": ("Дата:",),
    "fullname": ("Пациент:",),
    "birthdate": ("Дата рождения:",),
}
