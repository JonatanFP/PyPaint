import os
from tkinter import *
from tkinter.colorchooser import askcolor

from PIL import Image
from const import *


class PyPaint:
    selected_pen_size = 0.0
    color_draw = BLACK
    pen_size = 5.0

    def __init__(self, master):
        self.button1 = Button(root, text="Lápis", bg="black", fg="white", width=11, command=self.draw)
        self.button1.grid(row=0, column=0)
        self.button2 = Button(root, text="Borracha", bg="black", fg="white", width=11, command=self.erase)
        self.button2.grid(row=0, column=1)
        self.button3 = Button(root, text="Cor", bg="black", fg="white", width=11, command=self.choose_color)
        self.button3.grid(row=0, column=2)
        self.button4 = Button(root, text="Tamanho", bg="black", fg="white", width=11, command=self.size)
        self.button4.grid(row=0, column=3)
        self.button5 = Button(root, text="Salvar", bg="black", fg="white", width=11, command=self.name_img)
        self.button5.grid(row=0, column=4)
        self.button6 = Button(root, text="Limpar Tudo", bg="black", fg="white", width=11, command=self.clean_all)
        self.button6.grid(row=0, column=5)
        self.button7 = Button(root, text="Fechar", bg="black", fg="white", width=11, command=root.quit)
        self.button7.grid(row=0, column=6)

    def draw(self):
        canvas.bind(LEFT_BUTTON, self.step)

    def painting(self, event):
        canvas.create_line(self.x1, self.y1, event.x, event.y, width=self.pen_size, fill=self.color_draw,
                           capstyle=ROUND, smooth=TRUE, splinesteps=40)
        self.x1 = event.x
        self.y1 = event.y

    def step(self, event):
        self.x1 = event.x
        self.y1 = event.y
        canvas.bind(LEFT_BUTTON_MOTION, self.painting)

    def erase(self):
        canvas.bind(LEFT_BUTTON, self.step2)

    def erasing(self, event):
        canvas.create_line(self.x1, self.y1, event.x, event.y, width=self.pen_size, fill='white', capstyle=ROUND,
                           smooth=TRUE, splinesteps=30)
        self.x1 = event.x
        self.y1 = event.y

    def step2(self, event):
        self.x1 = event.x
        self.y1 = event.y
        canvas.bind(LEFT_BUTTON_MOTION, self.erasing)

    def clean_all(self):
        canvas.delete("all")

    def size(self):
        if root.counter == 0:
            self.button8 = Scale(root, from_=1, to=100, bg="white", fg="black", length=500, orient=HORIZONTAL,
                                 variable=self.selected_pen_size)
            self.button8.grid(row=1, columnspan=5)
            self.button9 = Button(root, text="Selecionar", bg="black", fg="white", width=11, command=self.select)
            self.button9.grid(row=1, column=5)
            self.button10 = Button(root, text="Cancelar", bg="black", fg="white", width=11, command=self.close_size)
            self.button10.grid(row=1, column=6)
            root.counter += 1
        else:
            self.close_size()

    def select(self):
        self.pen_size = self.selected_pen_size.get()
        self.close_size()

    def close_size(self):
        self.button8.grid_forget()
        self.button9.grid_forget()
        self.button10.grid_forget()
        root.counter = 0

    def name_img(self):
        if root.counter2 == 0:
            self.button13 = Button(root, text="Nome do Arquivo:", bg="black", fg="white", width=12)
            self.button13.grid(row=1, column=0)
            self.button14 = Entry(root)
            self.button14.grid(row=1, column=2)
            self.button11 = Button(root, text="Salvar", bg="black", fg="white", width=11, command=self.save_img)
            self.button11.grid(row=1, column=5)
            self.button12 = Button(root, text="Cancelar", bg="black", fg="white", width=11, command=self.close_save)
            self.button12.grid(row=1, column=6)
            root.counter2 += 1
        else:
            self.close_save()

    def save_img(self):
        canvas.postscript(file=self.button14.get() + '.eps')
        img = Image.open(self.button14.get() + '.eps')
        img.save(self.button14.get() + '.png', 'png')
        os.remove(self.button14.get() + '.eps')
        self.close_save()

    def close_save(self):
        self.button11.grid_forget()
        self.button12.grid_forget()
        self.button13.grid_forget()
        self.button14.grid_forget()
        root.counter2 = 0

    def choose_color(self):
        self.color_draw = askcolor(color=self.color_draw)[1]


root = Tk()
root.counter = 0
root.counter2 = 0
root.title("PyPaint")

canvas = Canvas(root, bg="white", width=WIDTH, height=HEIGHT)
canvas.grid(row=2, columnspan=7)
PyPaint(root)
root.mainloop()
