from tkinter import *


class Window_first:

    def __init__(self, title="Калькулятор разбавления самогона", resizable=(True, False)):
        self.window = Toplevel()
        self.window.title(title)
        self.window.resizable(resizable[1], resizable[1])
        self.window["bg"] = "White"
        self.our_button_1 = PhotoImage(file="icon-10.png").subsample(2, 2)
        self.our_button_2 = PhotoImage(file="icon-12.png").subsample(4, 4)

    def draw_label(self):

        Label(self.window, image=self.our_button_1).grid(row=0, column=0, columnspan=4, sticky=W)
        Label(self.window, text="Объем спирта: \n ", font=10).grid(row=1, column=0, sticky=W)
        Label(self.window, text="литр: \n ", font=10).grid(row=1, column=3)
        Entry(self.window, width=10, font=30, bg="White").grid(row=1, column=1)
        Label(self.window, text="Процент спирта до: \n ", font=10).grid(row=3, column=0, sticky=W)
        Label(self.window, text="%: \n ", font=10).grid(row=3, column=3)
        Entry(self.window, width=10, font=30).grid(row=3, column=1)
        Label(self.window, text="Процент после: \n", font=10).grid(row=4, column=0, sticky=W)
        Label(self.window, text="%: \n ", font=10).grid(row=4, column=3)
        Entry(self.window, width=10, font=30, bg="White").grid(row=4, column=1)
        Label(self.window, font=10, image=self.our_button_2).grid(row=0, rowspan=4, column=4, columnspan=2)



    def run(self):
        self.draw_label()
        self.window.mainloop()


if __name__ == "__main__":
    root = Window_first()
    root.run()
