from tkinter import *


class TopWindow:

    def __init__(self,  resizable=(True, False)):
        self.window = Toplevel()
        self.window.resizable(resizable[1], resizable[1])
        self.window["bg"] = "White"
        self.our_icon_1 = PhotoImage(file="icon-10.png").subsample(2, 2)
        self.our_icon_2 = PhotoImage(file="icon-12.png").subsample(4, 4)
        self.our_icon_3 = PhotoImage(file="icon-13.png").subsample(4, 4)
        self.grad_focus()
        self.Label_1 = Label(self.window, image=self.our_icon_1, bg="White")
        self.label_2 = Label(self.window, image=self.our_icon_2, bg="White")
        self.label_3 = Label(self.window, font=10, bg="White")
        self.Label_1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.label_2.grid(row=0, column=4, rowspan=3, columnspan=2)
        self.label_3.grid(row=0, column=0, columnspan=5)

    def grad_focus(self):

        self.window.grab_set()
        self.window.focus_set()

    def run(self):

        self.window.mainloop()


class WindowFirst(TopWindow):

    def __init__(self, title=None):
        super().__init__()
        self.window.title(title)
        self.entry_1 = Entry(self.window, width=10, bg="White")
        self.entry_2 = Entry(self.window, width=10, bg="White")
        self.entry_3 = Entry(self.window, width=10, bg="White")

    def draw_label(self):

        Label(self.window, text="Объем спирта:", font=10, bg="White").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="литр:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Процент спирта до:", font=10, bg="White").grid(row=2, column=0, sticky=W, padx=5,
                                                                                pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=2, column=3)
        Label(self.window, text="Процент после: ", font=10, bg="White").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=3, column=3)

    def draw_entry(self):

        self.entry_1.grid(row=1, column=1, sticky=EW)
        self.entry_2.grid(row=2, column=1, sticky=EW)
        self.entry_3.grid(row=3, column=1, sticky=EW)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=4, column=4, sticky=EW)
        Button(self.window, text="НАЗАД", bg="White", command=self.window.destroy).grid(row=4, column=0, sticky=W)

    def alcohol(self):

        try:
            self.label_2.configure(image=self.our_icon_3)
            p = self.entry_1.get()
            n = self.entry_2.get()
            m = self.entry_3.get()
            n, m = int(n), int(m)
            p = float(p)
            x = n * p / m - p
            self.label_3["text"] = "Вода " + str(round(x, 2)) + " лит."

        except ValueError:
            self.label_3["text"] = "Введите корректное значение"

    def grad_focus(self):
        super().grad_focus()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()
        self.window.mainloop()


class WindowSecond(TopWindow):

    def __init__(self, title=None):
        super().__init__()
        self.window.title(title)
        self.entry_1 = Entry(self.window, width=10, bg="White")
        self.entry_2 = Entry(self.window, width=10, bg="White")
        self.entry_3 = Entry(self.window, width=10, bg="White")
        self.entry_4 = Entry(self.window, width=10, bg="White")

    def draw_label(self):

        Label(self.window, text="Объем первого спирта:", font=10, bg="White").grid(row=1, column=0, sticky=W,
                                                                                   padx=5, pady=5)
        Label(self.window, text="литры:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Крепость первого спирта:", font=10, bg="White").grid(row=2, column=0, sticky=W,
                                                                                      padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=2, column=3)
        Label(self.window, text="Объем второго спирта:", font=10, bg="White").grid(row=3, column=0, sticky=W, padx=5,
                                                                                   pady=5)
        Label(self.window, text="литры:", font=10, bg="White").grid(row=3, column=3)
        Label(self.window, text="Крепость второго спирта:", font=10, bg="White").grid(row=4, column=0, sticky=W,
                                                                                      padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=4, column=3)

    def draw_entry(self):

        self.entry_1.grid(row=1, column=1, sticky=EW)
        self.entry_2.grid(row=2, column=1, sticky=EW)
        self.entry_3.grid(row=3, column=1, sticky=EW)
        self.entry_4.grid(row=4, column=1, sticky=EW)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=5, column=4, sticky=EW)
        Button(self.window, text="НАЗАД", bg="White", command=self.window.destroy).grid(row=5, column=0, sticky=W)

    def alcohol(self):

        try:
            self.label_2.configure(image=self.our_icon_3)
            first_liquid = self.entry_1.get()
            first_fortress = self.entry_2.get()
            second_liquid = self.entry_3.get()
            second_fortress = self.entry_4.get()
            first_liquid, second_liquid = float(first_liquid), float(second_liquid)
            first_fortress, second_fortress = int(first_fortress), int(second_fortress)
            fortress = (first_liquid * first_fortress + second_liquid * second_fortress) / (first_liquid + second_liquid)
            self.label_3["text"] = "\t Объем «голов»:  " + str(round(fortress, 2)) + " милилит."

        except ValueError:
            self.label_3["text"] = "Введите корректное значение"

    def grad_focus(self):
        super().grad_focus()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()
        self.window.mainloop()


class WindowThree(TopWindow):
    def __init__(self, title=None):
        super().__init__()
        self.window.title(title)
        self.entry_1 = Entry(self.window, width=10, bg="White")
        self.entry_2 = Entry(self.window, width=10, bg="White")
        self.entry_3 = Entry(self.window, width=10, bg="White")

    def draw_label(self):

        Label(self.window, text="Объем спирта:", font=10, bg="White").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="литр:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Крепость спитра-сырца:", font=10, bg="White").\
            grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=2, column=3)
        Label(self.window, text="Крепость на выходе: ", font=10, bg="White").\
            grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=3, column=3)

    def draw_entry(self):

        self.entry_1.grid(row=1, column=1, sticky=EW)
        self.entry_2.grid(row=2, column=1, sticky=EW)
        self.entry_3.grid(row=3, column=1, sticky=EW)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=4, column=4, sticky=EW)
        Button(self.window, text="НАЗАД", bg="White", command=self.window.destroy).grid(row=4, column=0, sticky=W)

    def alcohol(self):

        try:
            self.label_2.configure(image=self.our_icon_3)
            p = self.entry_1.get()
            n = self.entry_2.get()
            m = self.entry_3.get()
            n, m = int(n), int(m)
            self.label_3["text"] = round(m, 2)

        except ValueError:
            self.label_3["text"] = "Введите корректное значение"

    def grad_focus(self):
        super().grad_focus()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()
        self.window.mainloop()


class WindowFourth(TopWindow):

    def __init__(self, title=None):
        super().__init__()
        self.window.title(title)
        self.our_icon_3 = PhotoImage(file="icon-13.png").subsample(4, 4)
        self.entry_1 = Entry(self.window, width=10, bg="White")
        self.entry_2 = Entry(self.window, width=10, bg="White")

    def draw_label(self):

        Label(self.window, image=self.our_icon_1, bg="White").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="Объем воды:", font=10, bg="White").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="литр:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Количество сахара:", font=10, bg="White").\
            grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="кг:", font=10, bg="White").grid(row=2, column=3)

    def draw_entry(self):

        self.entry_1.grid(row=1, column=1, sticky=EW)
        self.entry_2.grid(row=2, column=1, sticky=EW)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=4, column=4, sticky=EW)
        Button(self.window, text="НАЗАД", bg="White", command=self.window.destroy).grid(row=4, column=0, sticky=W)

    def alcohol(self):

        try:
            self.label_2.configure(image=self.our_icon_3)
            water = self.entry_1.get()
            sugar = self.entry_2.get()
            water, sugar = int(water), int(sugar)
            volume = water + sugar * 0.6
            volume = float(volume)
            alcohol_content = (sugar * 0.6) / volume * 100
            self.label_3["text"] = "Объем браги  " + str(round(volume, 2)) + " лит." + \
                                   "\n Спиртуозность  " + str(round(alcohol_content, 2)) + " %"

        except ValueError:
            self.label_3["text"] = "Введите корректное значение"

    def grad_focus(self):
        super().grad_focus()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()
        self.window.mainloop()


class WindowFifth(TopWindow):

    def __init__(self, title=None):
        super().__init__()
        self.window.title(title)
        self.our_icon_3 = PhotoImage(file="icon-13.png").subsample(4, 4)
        self.entry_1 = Entry(self.window, width=10, bg="White")
        self.entry_2 = Entry(self.window, width=10, bg="White")
        self.entry_3 = Entry(self.window, width=10, bg="White")

    def draw_label(self):

        Label(self.window, text="Объем спирта-сырца:", font=10, bg="White").\
            grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="литров:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Крепость спирта-сырца", font=10, bg="White").\
            grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=2, column=3)
        Label(self.window, text="Головы: ", font=10, bg="White").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=3, column=3)

    def draw_entry(self):

        self.entry_1.grid(row=1, column=1, sticky=EW)
        self.entry_2.grid(row=2, column=1, sticky=EW)
        self.entry_3.grid(row=3, column=1, sticky=EW)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=4, column=4, sticky=EW)
        Button(self.window, text="НАЗАД", bg="White", command=self.window.destroy).grid(row=4, column=0, sticky=W)

    def alcohol(self):

        try:

            self.label_2.configure(image=self.our_icon_3)
            amount_of_alcohol = self.entry_1.get()
            alcohol_strength = self.entry_2.get()
            percentage_of_alcohol = self.entry_3.get()
            amount_of_alcohol, alcohol_strength = int(amount_of_alcohol), int(alcohol_strength)
            percentage_of_alcohol = int(percentage_of_alcohol)
            pure_alcohol = amount_of_alcohol * alcohol_strength / 100
            volume_of_heads = pure_alcohol * percentage_of_alcohol * 10
            self.label_3["text"] = "Объем чистого спирта:  " + str(round(pure_alcohol, 2)) + " лит." + \
                                   "\n Объем «голов»:  " + str(round(volume_of_heads, 2)) + " милилит."

        except ValueError:
            self.label_3["text"] = " Введите корректное значение"

    def grad_focus(self):
        super().grad_focus()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()
        self.window.mainloop()


class WindowSixth(TopWindow):

    def __init__(self, title=None):
        super().__init__()
        self.window.title(title)
        self.our_icon_3 = PhotoImage(file="icon-13.png").subsample(4, 4)
        self.entry_1 = Entry(self.window, width=10, bg="White")
        self.entry_2 = Entry(self.window, width=10, bg="White")

    def draw_label(self):

        Label(self.window, text="Темпиратура сырца:", font=10, bg="White").\
            grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="°С:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Показание ареометра:", font=10, bg="White").\
            grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="°:", font=10, bg="White").grid(row=2, column=3)

    def draw_entry(self):

        self.entry_1.grid(row=1, column=1, sticky=EW)
        self.entry_2.grid(row=2, column=1, sticky=EW)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=4, column=4, sticky=EW)
        Button(self.window, text="НАЗАД", bg="White", command=self.window.destroy).grid(row=4, column=0, sticky=W)

    def alcohol(self):

        try:

            self.label_2.configure(image=self.our_icon_3)
            # water = self.entry_1.get()
            # sugar = self.entry_2.get()
            # water, sugar = int(water), int(sugar)
            # volume = water + sugar * 0.6
            # volume = float(volume)
            # alcohol_content = (sugar * 0.6) / volume * 100
            # self.label_3["text"] = "Объем браги  " + str(round(volume, 2)) + " лит." + \
            #                        "\n Спиртуозность  " + str(round(alcohol_content, 2)) + " %"

        except ValueError:
            self.label_3["text"] = "Введите корректное значение"

    def grad_focus(self):
        super().grad_focus()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()
        self.window.mainloop()


if __name__ == "__main__":
    first = WindowFirst(title="Расчет")
    first.run()
    second = WindowSecond(title="Проба")
    second.run()
    fifth = WindowFifth(title="брага")
    fifth.run()
