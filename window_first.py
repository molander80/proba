from tkinter import *


class Window:
    def __init__(self, title="Калькулято самогонщика", resizable=(True, False)):
        self.tk = Tk()
        self.tk.title(title)
        self.tk.resizable(resizable[1], resizable[1])
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
               highlightthickness=0, bd=0, compound=TOP, activebackground="White").grid(row=0, column=0)

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

    def run(self):
        self.draw_widgest()
        self.tk.mainloop()



if __name__ == "__main__":
    window = Window()
    window.run()
