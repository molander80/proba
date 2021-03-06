from tect2 import *


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

        Button(self.tk, text="Калькулятор \n разбавления самогона", font=10, bg="White", image=self.our_button_2,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White",
               command=self.draw_button_1).grid(row=0, column=0)

        Button(self.tk, text="Калькулятор \n смешивания алкоголя", font=10, bg="White", image=self.our_button_4,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White",
               command=self.draw_button_2).grid(row=0, column=1)

        Button(self.tk, text="Калькулятор \n второй перегонки", font=10, bg="White", image=self.our_button_3,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White",
               command=self.draw_button_3).grid(row=0, column=2)

        Button(self.tk, text="Расчет параметров \n сахарной браги \n", font=10, bg="White", image=self.our_button_5,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White",
               command=self.draw_button_4).grid(row=1, column=0, sticky=EW)

        Button(self.tk, text="Калькулятор \n абсолютного спирта и \n отбора голов", font=10, bg="White",
               image=self.our_button_6,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White",
               command=self.draw_button_5).grid(row=1, column=1, sticky=EW)

        Button(self.tk, text="Калькулятор \n коррекции показаний \n ареометра", font=10, bg="White",
               image=self.our_button_8,
               highlightthickness=0, bd=0, compound=TOP, activebackground="White",
               command=self.draw_button_6).grid(row=1, column=2, sticky=EW)

    def draw_button_1(self):
        WindowFirst(title="Калькулятор разбавления самогона").run()

    def draw_button_2(self):

        WindowSecond(title="Калькулятор смешивания самогона").run()

    def draw_button_3(self):

        WindowThree(title="Калькулятор дробной перегонки спирта-сырца").run()

    def draw_button_4(self):

        WindowFourth(title="Расчет параметров сахарной браги").run()

    def draw_button_5(self):

        WindowFifth(title="Калькулятор абсолютного спирта и отбора голов").run()

    def draw_button_6(self):

        WindowSixth(title="Калькулятор коррекции показаний ареометра").run()

    def run(self):
        self.draw_widgest()
        self.tk.mainloop()


if __name__ == "__main__":
    window = Window()
    window.run()

