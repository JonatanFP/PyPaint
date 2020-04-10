import os
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image


class PyPaint:
    colordraw = "#000000"
    pensize = 5.0


    def __init__(self, master):
        self.button1 = Button(root, text="Lápis", bg="black", fg="white", width=11, command=self.draw)
        self.button1.grid(row=0, column=0)
        self.button2 = Button(root, text="Borracha", bg="black", fg="white", width=11, command=self.erase)
        self.button2.grid(row=0, column=1)
        self.button3 = Button(root, text="Cor", bg="black", fg="white", width=11, command=self.choosecolor)
        self.button3.grid(row=0, column=2)
        self.button4 = Button(root, text="Tamanho", bg="black", fg="white", width=11, command=self.size)
        self.button4.grid(row=0, column=3)
        self.button5 = Button(root, text="Salvar", bg="black", fg="white", width=11, command=self.nameimg)
        self.button5.grid(row=0, column=4)
        self.button6 = Button(root, text="Limpar Tudo", bg="black", fg="white", width=11, command=self.cleanAll)
        self.button6.grid(row=0, column=5)
        self.button7 = Button(root, text="Fechar", bg="black", fg="white", width=11, command=root.quit)
        self.button7.grid(row=0, column=6)

    def draw(self):
        c.bind('<Button-1>', self.step)

    def painting(self, event):

        c.create_line(self.x1, self.y1, event.x, event.y, width=self.pensize, fill=self.colordraw, capstyle=ROUND, smooth=TRUE, splinesteps=40)
        self.x1 = event.x
        self.y1 = event.y

    def step(self, event):
        self.x1=event.x
        self.y1=event.y
        c.bind('<B1-Motion>', self.painting)


    def erase(self):
        c.bind('<Button-1>', self.step2)


    def erasing(self, event):
        c.create_line(self.x1, self.y1, event.x, event.y, width=self.pensize, fill='white', capstyle=ROUND, smooth=TRUE, splinesteps=30)
        self.x1 = event.x
        self.y1 = event.y


    def step2(self, event):
        self.x1 = event.x
        self.y1 = event.y
        c.bind('<B1-Motion>', self.erasing)


    def cleanAll(self):
        c.delete("all")


    def size(self):
        if root.counter == 0:
            self.button8 = Scale(root, from_=1, to=100, bg="white", fg="black", length=500, orient=HORIZONTAL, variable=valor)
            self.button8.grid(row=1, columnspan=5)
            self.button9 = Button(root, text="Selecionar", bg="black", fg="white", width=11, command=self.select)
            self.button9.grid(row=1, column=5)
            self.button10 = Button(root, text="Cancelar", bg="black", fg="white", width=11, command=self.closesize)
            self.button10.grid(row=1, column=6)
            root.counter += 1
        else:
            self.closesize()


    def select(self):
        self.pensize = valor.get()
        self.closesize()

    def closesize(self):
        self.button8.grid_forget()
        self.button9.grid_forget()
        self.button10.grid_forget()
        root.counter = 0

    def nameimg(self):
        if root.counter2 == 0:
            self.button13 = Button(root, text="Nome do Arquivo:", bg="black", fg="white", width=12)
            self.button13.grid(row=1, column=0)
            self.button14 = Entry(root)
            self.button14.grid(row=1, column=2)
            self.button11 = Button(root, text="Salvar", bg="black", fg="white", width=11, command=self.saveimg)
            self.button11.grid(row=1, column=5)
            self.button12 = Button(root, text="Cancelar", bg="black", fg="white", width=11, command=self.closesave)
            self.button12.grid(row=1, column=6)
            root.counter2 += 1
        else:
            self.closesave()

    def saveimg(self):
        c.postscript(file = self.button14.get() + '.eps')
        img = Image.open(self.button14.get() +'.eps')
        img.save(self.button14.get() + '.png', 'png')
        os.remove(self.button14.get() + '.eps')
        self.closesave()

    def closesave(self):
        self.button11.grid_forget()
        self.button12.grid_forget()
        self.button13.grid_forget()
        self.button14.grid_forget()
        root.counter2 = 0


    def choosecolor(self):
        self.colordraw = askcolor(color=self.colordraw)[1]


root = Tk()
root.counter = 0
root.counter2 = 0
valor = DoubleVar()
root.title('PyPaint')
c = Canvas(root, bg='white', width=1000, height=700)
c.grid(row=2, columnspan=7)
PyPaint(root)
root.mainloop()
