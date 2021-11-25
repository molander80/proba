from tkinter import *


class Window:
    def __init__(self, title="Калькулято самогонщика", resizable=(True, False)):
        self.tk = Tk()
        self.tk.title(title)
        self.tk.resizable(resizable[1], resizable[1])
        self.tk["bg"] = "White"
        self.our_button_1 = PhotoImage(file="icon-1.png")
        self.our_button_2 = PhotoImage(file="icon-2.png")
        self.our_button_3 = PhotoImage(file="icon-3.png")
        self.our_button_4 = PhotoImage(file="icon-4.png")
        self.our_button_5 = PhotoImage(file="icon-5.png")
        self.our_button_6 = PhotoImage(file="icon-6.png")
        self.our_button_7 = PhotoImage(file="icon-7.png")
        self.our_button_8 = PhotoImage(file="icon-8.png")

    def draw_widgest(self):

        Button(self.tk, text="Калькулятор \n разбавления самогона", font=10, bg="White", image=self.our_button_4,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White", command=self.draw_button).grid(row=0, column=0)

        Button(self.tk, text="Калькулятор \n смешивания алкоголя", font=10, bg="White", image=self.our_button_2,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White").grid(row=0, column=1)

        Button(self.tk, text="Калькулятор \n второй перегонки", font=10, bg="White", image=self.our_button_3,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White").grid(row=0, column=2)

        Button(self.tk, text="Таблица содержания \n сахара", font=10, bg="White", image=self.our_button_1,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White").grid(row=0, column=3)

        Button(self.tk, text="Калькулятор расчета \n сахарной браги \n", font=10, bg="White", image=self.our_button_5,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White").grid(row=1, column=0, sticky=EW)

        Button(self.tk, text="Калькулятор замены \n сахара глюкозой \n", font=10, bg="White", image=self.our_button_6,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White").grid(row=1, column=1, sticky=EW)

        Button(self.tk, text="Калькулятор \n абсолютного спирта и \n отбора голов", font=10, bg="White", image=self.our_button_7,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White").grid(row=1, column=2, sticky=EW)

        Button(self.tk, text="Калькулятор \n коррекции показаний \n ареометра", font=10, bg="White", image=self.our_button_8,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White").grid(row=1, column=3, sticky=EW)

    def draw_button(self):

        first = WindowFirst()
        first.draw_label()
        first.run()

    def run(self):
        self.draw_widgest()
        self.tk.mainloop()


class WindowFirst:

    def __init__(self, title="Калькулятор разбавления самогона", resizable=(True, False)):
        self.window = Toplevel()
        self.window.title(title)
        self.window.resizable(resizable[1], resizable[1])
        self.window["bg"] = "White"
        self.our_icon_1 = PhotoImage(file="icon-10.png").subsample(2, 2)
        self.our_icon_2 = PhotoImage(file="icon-12.png").subsample(4, 4)
        self.our_icon_3 = PhotoImage(file="icon-13.png").subsample(4, 4)

    def draw_label(self):

        Label(self.window, image=self.our_icon_1, bg="White").grid(row=0, column=0, sticky=W)
        Label(self.window, text="Объем спирта:", font=10, bg="White").grid(row=1, column=0, sticky=W)
        Label(self.window, text="литр:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Процент спирта до:", font=10, bg="White").grid(row=2, column=0, sticky=W)
        Label(self.window, text="%:", font=10, bg="White").grid(row=2, column=3)
        Label(self.window, text="Процент после: ", font=10, bg="White").grid(row=3, column=0, sticky=W)
        Label(self.window, text="%:", font=10, bg="White").grid(row=3, column=3)
        Label(self.window, image=self.our_icon_2, bg="White").grid(row=0, column=4, rowspan=3, columnspan=2)

    def draw_entry(self):

        Entry(self.window, width=10, font=10, bg="White").grid(row=1, column=1)
        Entry(self.window, width=10, font=20, bg="White").grid(row=2, column=1)
        Entry(self.window, width=10, font=30, bg="White").grid(row=3, column=1)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=4, column=1)

    def alcohol(self):

        Label(self.window, font=10, image=self.our_icon_3, bg="White").grid(row=0, column=4, rowspan=3, columnspan=2)

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()
        self.window.mainloop()


if __name__ == "__main__":
    root = Window()
    root.run()


