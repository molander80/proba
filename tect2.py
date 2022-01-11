from tkinter import *


class WindowFirst:

    def __init__(self, title=None, resizable=(True, False)):
        self.window = Tk()
        self.window.title(title)
        self.window.resizable(resizable[1], resizable[1])
        self.window["bg"] = "White"
        self.our_icon_1 = PhotoImage(file="icon-10.png").subsample(2, 2)
        self.our_icon_2 = PhotoImage(file="icon-12.png").subsample(4, 4)
        self.our_icon_3 = PhotoImage(file="icon-13.png").subsample(4, 4)
        self.entry_1 = Entry(self.window, width=10, bg="White")
        self.entry_2 = Entry(self.window, width=10, bg="White")
        self.entry_3 = Entry(self.window, width=10, bg="White")
        self.grad_focus()
        self.label_2 = Label(self.window, image=self.our_icon_2, bg="White")
        self.label_3 = Label(self.window, font=10, bg="White")

    def draw_label(self):

        Label(self.window, image=self.our_icon_1, bg="White").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="Объем спирта:", font=10, bg="White").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="литр:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Процент спирта до:", font=10, bg="White").grid(row=2, column=0, sticky=W, padx=5,
                                                                                pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=2, column=3)
        Label(self.window, text="Процент после: ", font=10, bg="White").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=3, column=3)
        self.label_2.grid(row=0, column=4, rowspan=3, columnspan=2)
        self.label_3.grid(row=0, column=0, columnspan=3)

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
            self.label_3["text"] = round(x, 2)

        except ValueError:
            self.label_3["text"] = "\t Введите корректное значение"
            #self.lebel_4.grid_forget()

    def grad_focus(self):

        self.window.grab_set()
        self.window.focus_set()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()
        self.window.mainloop()



class WindowSecond:

    def __init__(self, title=None, resizable=(True, False)):
        self.window = Toplevel()
        self.window.title(title)
        self.window.resizable(resizable[1], resizable[1])
        self.window["bg"] = "White"
        self.our_icon_1 = PhotoImage(file="icon-10.png").subsample(2, 2)
        self.our_icon_2 = PhotoImage(file="icon-12.png").subsample(4, 4)
        self.our_icon_3 = PhotoImage(file="icon-13.png").subsample(4, 4)
        self.grad_focus()

    def draw_label(self):

        Label(self.window, image=self.our_icon_1, bg="White").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="Объем первого спирта:", font=10, bg="White").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="литры:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Крепость первого спирта:", font=10, bg="White").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=2, column=3)
        Label(self.window, text="Объем второго спирта:", font=10, bg="White").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="литры:", font=10, bg="White").grid(row=3, column=3)
        Label(self.window, text="Крепость второго спирта:", font=10, bg="White").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=4, column=3)
        Label(self.window, image=self.our_icon_2, bg="White").grid(row=0, column=4, rowspan=3, columnspan=2)

    def draw_entry(self):
        Entry(self.window, width=10, bg="White").grid(row=1, column=1, sticky=EW)
        Entry(self.window, width=10, bg="White").grid(row=2, column=1, sticky=EW)
        Entry(self.window, width=10, bg="White").grid(row=3, column=1, sticky=EW)
        Entry(self.window, width=10, bg="White").grid(row=4, column=1, sticky=EW)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=5, column=4, sticky=EW)
        Button(self.window, text="НАЗАД", bg="White", command=self.window.destroy).grid(row=5, column=0, sticky=W)

    def alcohol(self):

        Label(self.window, font=10, image=self.our_icon_3, bg="White").grid(row=0, column=4, rowspan=3, columnspan=2)

    def grad_focus(self):

        self.window.grab_set()
        self.window.focus_set()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()


class WindowFifth:

    def __init__(self, title=None, resizable=(True, False)):
        self.window = Toplevel()
        self.window.title(title)
        self.window.resizable(resizable[1], resizable[1])
        self.window["bg"] = "White"
        self.our_icon_1 = PhotoImage(file="icon-10.png").subsample(2, 2)
        self.our_icon_2 = PhotoImage(file="icon-12.png").subsample(4, 4)
        self.our_icon_3 = PhotoImage(file="icon-13.png").subsample(4, 4)
        self.entry_1 = Entry(self.window, width=10, bg="White")
        self.entry_2 = Entry(self.window, width=10, bg="White")
        self.grad_focus()
        self.label_2 = Label(self.window, image=self.our_icon_2, bg="White")
        self.label_3 = Label(self.window, font=10, bg="White")

    def draw_label(self):

        Label(self.window, image=self.our_icon_1, bg="White").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="Объем спирта:", font=10, bg="White").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="литр:", font=10, bg="White").grid(row=1, column=3)
        Label(self.window, text="Процент спирта до:", font=10, bg="White").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(self.window, text="%:", font=10, bg="White").grid(row=2, column=3)
        self.label_2.grid(row=0, column=4, rowspan=3, columnspan=2)
        self.label_3.grid(row=4, column=4, columnspan=2)

    def draw_entry(self):

        self.entry_1.grid(row=1, column=1, sticky=EW)
        self.entry_2.grid(row=2, column=1, sticky=EW)

    def draw_button(self):

        Button(self.window, text="ПОСЧИТАТЬ", command=self.alcohol, bg="White").grid(row=4, column=4, sticky=EW)
        Button(self.window, text="НАЗАД", bg="White", command=self.window.destroy).grid(row=4, column=0, sticky=W)

    def alcohol(self):

        Label(self.window, font=10, image=self.our_icon_3, bg="White").grid(row=0, column=4, rowspan=3, columnspan=2)

    def grad_focus(self):

        self.window.grab_set()
        self.window.focus_set()

    def run(self):

        self.draw_label()
        self.draw_button()
        self.draw_entry()


if __name__ == "__main__":
    second = WindowFirst(title="Расчет")
    second.run()
