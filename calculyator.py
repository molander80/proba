from tkinter import *


class Window_first:

    def __init__(self, title="Калькулятор Самогонщика"):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("300x180")

        self.lebel_0 = Label(self.window, font=10)
        self.lebel_1 = Label(self.window, text="Начальная спиртуозность", font=5)
        self.lebel_2 = Label(self.window, text="Объем", font=10)
        self.lebel_3 = Label(self.window, font=10)

        self.lebel_0.grid(row=0, columnspan=3)
        self.lebel_1.grid(row=1, columnspan=2, sticky=EW)
        self.lebel_2.grid(row=2, column=0, sticky=EW)
        self.lebel_3.grid(row=0, column=2)

        self.entry_1 = Entry(self.window, width=3, font=10)
        self.entry_2 = Entry(self.window, width=3, font=10)
        self.entry_3 = Entry(self.window, width=3, font=10)

        self.entry_1.grid(row=1, column=2)
        self.entry_2.grid(row=2, column=2)
        self.entry_3.grid(row=3, column=2)
        self.button_1 = Button(self.window, text="Расчитать", font=10, command=self.alcohol_content)
        self.button_1.grid(row=5, column=1, columnspan=2, sticky=EW)

    def alcohol_content(self):
        """
        calculation of alcohol dilution with water
        """
        try:
            n, p, m = (self.entry_1.get(), self.entry_2.get(), self.entry_3.get())
            n, m = int(n), int(m)
            p = float(p)
            x = n * p / m - p
            self.lebel_3.grid(row=0, column=2)
            self.lebel_3["text"] = round(x, 2)

        except ValueError:
            self.lebel_3.grid(row=0, column=0, columnspan=3)
            self.lebel_3["text"] = "Введите корректное значение"

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":

    second = Window_first(title="Самогонщика", self.lebel_3[text="proba"])
    second.run()