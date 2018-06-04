from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):
        self.parent.title("Paint")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(6, weight=2)
        self.rowconfigure(2, weight=1)
        self.canv = Canvas(self, bg="#FFFFF0")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>", self.draw)
        ###
        color_lab = Label(self, text="Цвет: ")
        color_lab.grid(row=0, column=0, padx=6)
        red_btn = Button(self, text="Красный", width=15,
                         command=lambda: self.set_color("#FF0000"))
        red_btn.grid(row=0, column=1)
        green_btn = Button(self, text="Зеленый", width=15,
                         command=lambda: self.set_color("#008000"))
        green_btn.grid(row=0, column=2)
        blue_btn = Button(self, text="Синий", width=15,
                         command=lambda: self.set_color("#0000FF"))
        blue_btn.grid(row=0, column=3)
        yellow_btn = Button(self, text="Желтый", width=15,
                         command=lambda: self.set_color("#FFFF00"))
        yellow_btn.grid(row=0, column=4)
        black_btn = Button(self, text="Черный", width=15,
                         command=lambda: self.set_color("#000000"))
        black_btn.grid(row=0, column=5)
        ###
        clear_btn = Button(self, text="Очистить", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)
        size_lab = Label(self, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="2", width=15,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)
        two_btn = Button(self, text="5", width=15,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)
        three_btn = Button(self, text="10", width=15,
                         command=lambda: self.set_brush_size(10))
        three_btn.grid(row=1, column=3)
        ###

def main():
    root = Tk()
    root.geometry("1400x800+300+300")
    app = Paint(root)
    root.mainloop()

if __name__ == "__main__":
    main()