import tkinter as tk
import app.todo.template.text as text
from tkinter import messagebox as mb


class Label(tk.Label):
    def __init__(self, text):
        super().__init__(root, text=text, bg=main_color, font=main_font)

    def grid(self, row, column):
        super().grid(row=row, column=column, padx=40, pady=5, sticky="e")


class Entry(tk.Entry):
    def __init__(self, width):
        super().__init__(root, bg=relief_color, width=width, font=main_font)

    def grid(self, row, column):
        super().grid(row=row, column=column, pady=5, sticky="w")


class Button(tk.Button):
    def __init__(self, text, command):
        super().__init__(root, text=text, bg=relief_color, width=10, height=2, font=main_font, command=command)

    def grid(self, row, column):
        super().grid(row=row, column=column, padx=40, pady=5, sticky="e")


def get_start():
    patient_data["имя"] = entries[0].get()
    patient_data["дата рождения"] = entries[1].get()
    patient_data["жалобы"] = entries[2].get()
    patient_data["голова"] = entries[3].get()
    patient_data["грудь"] = entries[4].get()
    patient_data["родничок"] = entries[5].get()
    patient_data["аллергия"] = entries[6].get()

    for char in labels + entries + buttons:
        char.destroy()

    get_check_buttons()


def get_check_buttons():
    for check in check_buttons:

    pass

    """
    
# second screen- status
def checks_1():
    global checks1, btn
    checks1 = []
    for c in range(len(t1)):
        checks1.append(
            tk.Checkbutton(root, text=f"{t1[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var1[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks1[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_1)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_1():
    for c in range(len(t1)):
        if var1[c].get() == False:
            t1[c] = ""
    for object in checks1:
        object.destroy()
    btn.destroy()
    checks_2()


def checks_2():
    global checks2, btn
    checks2 = []
    for c in range(len(t2)):
        checks2.append(
            tk.Checkbutton(root, text=f"{t2[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var2[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks2[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_2)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_2():
    for c in range(len(t2)):
        if var2[c].get() == False:
            t2[c] = ""
    for object in checks2:
        object.destroy()
    btn.destroy()
    checks_3()


def checks_3():
    global checks3, btn
    checks3 = []
    for c in range(len(t3)):
        checks3.append(
            tk.Checkbutton(root, text=f"{t3[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var3[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks3[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_3)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_3():
    for c in range(len(t3)):
        if var3[c].get() == False:
            t3[c] = ""
    for object in checks3:
        object.destroy()
    btn.destroy()
    checks_4()


def checks_4():
    global checks4, btn
    checks4 = []
    for c in range(len(t4)):
        checks4.append(
            tk.Checkbutton(root, text=f"{t4[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var4[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks4[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_4)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_4():
    for c in range(len(t4)):
        if var4[c].get() == False:
            t4[c] = ""
    for object in checks4:
        object.destroy()
    btn.destroy()
    checks_5()


def checks_5():
    global checks5, btn
    checks5 = []
    for c in range(len(t5)):
        checks5.append(
            tk.Checkbutton(root, text=f"{t5[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var5[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks5[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_5)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_5():
    for c in range(len(t5)):
        if var5[c].get() == False:
            t5[c] = ""
    for object in checks5:
        object.destroy()
    btn.destroy()
    diagnosis()


# third screen- diagnosis
def diagnosis():
    global checks6, btn
    checks6 = []
    for c in range(len(t6)):
        checks6.append(
            tk.Checkbutton(root, text=f"{t6[c][:60]}", bg=maincolor, anchor="w", padx=10, width=52, variable=var6[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks6[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_6)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_6():
    for c in range(len(t6)):
        if var6[c].get() == False:
            t6[c] = ""
            t7[c] = ""
    for object in checks6:
        object.destroy()
    btn.destroy()
    prescription_1()


# fourth screen- prescription
def prescription_1():
    global checks8, btn
    checks8 = []
    for c in range(len(t8)):
        checks8.append(
            tk.Checkbutton(root, text=f"{t8[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var8[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks8[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_8)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_8():
    for c in range(len(t8)):
        if var8[c].get() == False:
            t8[c] = ""
    for object in checks8:
        object.destroy()
    btn.destroy()
    prescription_2()


def prescription_2():
    global checks9, btn
    checks9 = []
    for c in range(len(t9)):
        checks9.append(
            tk.Checkbutton(root, text=f"{t9[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var9[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks9[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_9)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_9():
    for c in range(len(t9)):
        if var9[c].get() == False:
            t9[c] = ""
    for object in checks9:
        object.destroy()
    btn.destroy()
    prescription_3()


def prescription_3():
    global checks10, btn
    checks10 = []
    for c in range(len(t10)):
        checks10.append(
            tk.Checkbutton(root, text=f"{t10[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var10[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        elif c >= 40 and c < 60:
            rw = c - 40;
            col = 2
        checks10[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Далее", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_10)
    btn.grid(row=20, column=0, padx=20, pady=40)


def get_entry_10():
    for c in range(len(t10)):
        if var10[c].get() == False:
            t10[c] = ""
    for object in checks10:
        object.destroy()
    btn.destroy()
    prescription_4()


def prescription_4():
    global checks11, btn, final_btn, last_column
    last_column = 0
    checks11 = []
    for c in range(len(t11)):
        checks11.append(
            tk.Checkbutton(root, text=f"{t11[c][:60]}".replace("\n", ""), bg=maincolor, anchor="w", padx=10, width=52,
                           variable=var11[c],
                           onvalue=1, offvalue=0))
        if c < 20:
            rw = c;
            col = 0
        elif c >= 20 and c < 40:
            rw = c - 20;
            col = 1
        checks11[c].grid(row=rw, column=col)
    btn = tk.Button(root, text="Добавить", bd=5, font=("Times New Roman", 12), width=10, height=2, command=get_entry_11)
    btn.grid(row=20, column=0, padx=20, pady=40)
    final_btn = tk.Button(root, text="Готово", bd=5, font=("Times New Roman", 12), width=10, height=2, bg="#73a628",
                          command=ask_about_card)
    final_btn.grid(row=20, column=2, padx=20, pady=40)


def get_entry_11():
    global t12, last_column
    for c in range(len(t11)):
        if var11[c].get() and t11[c] != "":
            t12.append(t11[c])
            checks11[c].destroy()
            tk.Label(root, text=f"Добавлено: {t11[c][:26]}", bg=maincolor, anchor="w", padx=10, width=52).grid(
                row=last_column, column=2)
            t11[c] = ""
            last_column += 1

    """


# root config
root = tk.Tk()
root.title("Назначение невролога")
root.geometry("1280x640+40+40")
root.resizable(False, False)
main_color = "#80C060"
relief_color = "#B0F090"
main_font = ("Arial", 14)
root.config(bg=main_color)


patient_data = dict.fromkeys((
    "имя",
    "дата рождения",
    "жалобы",
    "голова",
    "грудь",
    "родничок",
    "аллергия"
))

check_buttons = (
    text.status_text_1,
    text.status_text_2,
    text.status_text_3,
    text.status_text_4,
    text.status_text_5,
    text.diagnosis_dict.keys(),
    text.prescription_text_1,
    text.prescription_text_2,
    text.prescription_text_3,
    text.prescription_text_4,
)


# main body
labels = (
    Label("Пациент:"),
    Label("Дата рождения:"),
    Label("Жалобы:"),
    Label("Голова, см:"),
    Label("Грудь, см:"),
    Label("Большой родничок, мм:"),
    Label("Аллергические реакции:"),
)

entries = (
    Entry(70),
    Entry(70),
    Entry(70),
    Entry(10),
    Entry(10),
    Entry(10),
    Entry(70),
)

buttons = (
    Button("Далее", get_start),
)

row = 0

for label, entry in zip(labels, entries):
    label.grid(row, 0)
    entry.grid(row, 1)
    row += 1

for button in buttons:
    button.grid(row, 0)
    row += 1


root.mainloop()
print(patient_data)
