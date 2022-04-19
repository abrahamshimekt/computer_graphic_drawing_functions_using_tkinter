import tkinter
from tkinter import *
import math

functions = []

window = Tk()
window.geometry("900x700")
intro = Label(window, text="Welcome to my project", font=40, )
choice = Label(window, text="choose functions >>>", font=5)
drawing_board = tkinter.Canvas(window, bg="teal", width=600, height=400)


def drawSin():
    xLast = 0
    yLast = 200
    for x in range(1, 600):
        y = 200 + 40 * math.sin(x / 20)
        drawing_board.create_line(xLast, yLast, x, y, fill="red")
        xLast = x
        yLast = y


def drawCosine():
    xLast = 0
    yLast = 200
    for x in range(1, 600):
        y = 200 + 40 * math.cos(x / 20)
        drawing_board.create_line(xLast, yLast, x, y)
        xLast = x
        yLast = y


def drawQuadratic():
    xLast = 300
    yLast = 200
    for x in range(1, 600):
        y = 200 + math.pow(x, 2)
        drawing_board.create_line(xLast, yLast, x, y, fill='white')
        xLast = x
        yLast = y


def draw(num1, num2):
    if num1 == 2:
        drawSin()
    if num2 == 3:
        drawCosine()


for i in range(6):
    option = IntVar()
    option.set(0)
    functions.append(option)

quadratic = Checkbutton(window, text=" X^2", variable=functions[0], bg="orange")

cubic = Checkbutton(window, text=" X^3", variable=functions[1], bg="orange")
sin = Checkbutton(window, text="sin(x)", variable=functions[2], bg="orange")
cosine = Checkbutton(window, text="cos(x)", variable=functions[3], bg="orange")
log = Checkbutton(window, text="log(x)", variable=functions[4], bg="orange")
exponential = Checkbutton(window, text=" 2^x", variable=functions[5], bg="orange")
draw_button = Button(window, text="Draw", bg='teal', command=lambda: draw(2, 3))
# drawing_frame = LabelFrame(window, border=5.0, background="black", height=400, width=650)
intro.grid(row=0, column=1, columnspan=6, padx=40, pady=20)
choice.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
quadratic.grid(row=2, column=0, padx=10, pady=10)
cubic.grid(row=2, column=1, padx=10, pady=10)
sin.grid(row=2, column=2, padx=10, pady=10)
cosine.grid(row=3, column=0, padx=10, pady=10)
log.grid(row=3, column=1, padx=10, pady=10)
exponential.grid(row=3, column=2, padx=10, pady=10)
# drawing_frame.grid(row=5, column=3, columnspan=3, sticky="NSEW")
draw_button.grid(row=4, column=0, padx=10, pady=10)
drawing_board.grid(row=5, column=3, columnspan=3)
window.mainloop()
