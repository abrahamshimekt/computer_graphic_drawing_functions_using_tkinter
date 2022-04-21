from tkinter import *
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np


def init():
    pygame.init()
    display = (600, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)


def draw_coordinate():
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 100.0)
    glVertex2f(0.0, -100.0)
    glVertex2f(100.0, 0.0)
    glVertex2f(-100.0, 0.0)
    glEnd()


def draw_quadratic():
    x = np.linspace(-10, 10, 1000)
    y = np.power(x, 2)
    for a, b in zip(x, y):
        glVertex2f(a, b)


def draw_cubic():
    x = np.linspace(-10, 10, 1000)
    y = np.power(x, 3)
    for a, b in zip(x, y):
        glVertex2f(a, b)


def draw_log():
    x = np.linspace(-1, 1, 100)
    y = np.log2(x)
    for a, b in zip(x, y):
        glVertex2f(a, b)


def draw_sin():
    x = np.linspace(-10, 10, 1000)
    y = np.sin(x)
    for a, b in zip(x, y):
        glVertex2f(a, b)


def draw_cosine():
    x = np.linspace(-10, 10, 1000)
    y = np.cos(x)
    for a, b in zip(x, y):
        glVertex2f(a, b)


def draw_power():
    x = np.linspace(-10, 10, 1000)
    y = np.power(2, x)
    for a, b in zip(x, y):
        glVertex2f(a, b)


def draw():
    if var0.get():
        glColor3f(1.0, 1.0, 0.0)
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        draw_quadratic()
        glEnd()
    if var1.get():
        glColor3f(1.0, 0.0, 1.0)
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        draw_cubic()
        glEnd()
    if var2.get():
        glColor3f(0.0, 1.0, 0.0)
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        draw_sin()
        glEnd()
    if var3.get():
        glColor3f(0.0, 1.0, 1.0)
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        draw_cosine()
        glEnd()
    if var4.get():
        glColor3f(0.5, 0.5, 0.5)
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        draw_log()
        glEnd()
    if var5.get():
        glColor3f(1.0, 1.0, 0.8)
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        draw_power()
        glEnd()
    draw_coordinate()
    glFlush()


window = Tk()
window.geometry("550x350")
intro = Label(window, text="Welcome to my project", font=40, )
choice = Label(window, text="choose functions", font=5)

var0 = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
quadratic = Checkbutton(window, text=" X^2", variable=var0, onvalue=True, offvalue=False, bg="orange")
cubic = Checkbutton(window, text=" X^3", variable=var1, onvalue=True, offvalue=False, bg="orange")
sin = Checkbutton(window, text="sin(x)", variable=var2, onvalue=True, offvalue=False, bg="orange")
cosine = Checkbutton(window, text="cos(x)", variable=var3, onvalue=True, offvalue=False, bg="orange")
log = Checkbutton(window, text="log(x)", variable=var4, onvalue=True, offvalue=False, bg="orange")
exponential = Checkbutton(window, text=" 2^x", variable=var5, onvalue=True, offvalue=False, bg="orange")

def draw_again():
    pygame.display.flip()
    var0.set(False)
    var1.set(False)
    var2.set(False)
    var3.set(False)
    var4.set(False)
    var5.set(False)
def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()
        pygame.time.wait(10)
        window.update()


again = Button(window, text="draw again", command=draw_again,bg="red")
draw_button = Button(window, text="Draw", bg='teal', command=main)
intro.grid(row=0, column=1, columnspan=6, padx=40, pady=20)
choice.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
quadratic.grid(row=2, column=0, padx=10, pady=10)
cubic.grid(row=2, column=1, padx=10, pady=10)
sin.grid(row=2, column=2, padx=10, pady=10)
cosine.grid(row=3, column=0, padx=10, pady=10)
log.grid(row=3, column=1, padx=10, pady=10)
exponential.grid(row=3, column=2, padx=10, pady=10)
draw_button.grid(row=4, column=0, padx=10, pady=10)
again.grid(row=4, column=1, padx=10, pady=10)
window.mainloop()
