from tkinter import *  # from tkinter module import all classes
import pygame  # import a pygame class
from OpenGL.GL import *  # from python opengl.gl module import all classes
from OpenGL.GLU import *  # from opengl.glu module import all classes
from pygame.locals import *  # from pygame.locals import all class
import numpy as np  # import a python numerical library

window = Tk()  # tkinter window
window.geometry("400x300")  # dimension for tkinter window
window.title("grapher")  # name for tkinter window

""" Init function initialize the pygame display window with width, height and colors
"""


def init():
    pygame.init()
    display = (600, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)


""" Draw_coordinate function draws the x,y coordinate when the pygame window displayed by the draw function
"""


def draw_coordinate():
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(0.0, 100.0)
    glVertex2f(0.0, -100.0)
    glVertex2f(100.0, 0.0)
    glVertex2f(-100.0, 0.0)


""" The draw_quadratic function draw a polynomial function with degree of 2 turning point at (0,0) and concave upward 
"""


def draw_quadratic():
    x = np.linspace(-10, 10, 1000)
    y = np.power(x, 2)
    for a, b in zip(x, y):
        glVertex2f(a, b)


""" The draw_quadratic function draw a polynomial function with degree of 3 turning point at (0,0) and monotonically increasing
"""


def draw_cubic():
    x = np.linspace(-10, 10, 1000)
    y = np.power(x, 3)
    for a, b in zip(x, y):
        glVertex2f(a, b)


""" The draw_log function draws the function with base e which is a natural logarithmic function
"""


def draw_log():
    x = np.linspace(0, 10, 1000)
    y = np.log(x)
    for a, b in zip(x, y):
        glVertex2f(a, b)


""" Draw_sin function draws a sin trigonometric function that has an amplitude of 1
"""


def draw_sin():
    x = np.linspace(-360, 360, 1000)
    y = np.sin(x)
    for a, b in zip(x, y):
        glVertex2f(a, b)


"""Draw_cosine function draws a cosine trigonometric function that has an amplitude of 1
"""


def draw_cosine():
    x = np.linspace(-360, 360, 1000)
    y = np.cos(x)
    for a, b in zip(x, y):
        glVertex2f(a, b)


"""Draw_power function draws a power mathematical function 2^x
"""


def draw_power():
    x = np.linspace(-10, 10, 1000)
    y = np.power(2, x)
    for a, b in zip(x, y):
        glVertex2f(a, b)


var0 = IntVar()  # integer variable for quadratic
var1 = IntVar()  # integer variable for cubic
var2 = IntVar()  # integer variable for sin
var3 = IntVar()  # integer variable for function
var4 = IntVar()  # integer variable for log
var5 = IntVar()  # integer variable for exponential

""" This function draws functions based on the if condition by getting the var value from check buttons
"""


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
        glColor3f(0.0, 0.0, 1.0)
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        draw_log()
        glEnd()
    if var5.get():
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        draw_power()
        glEnd()
    glBegin(GL_LINES)
    draw_coordinate()
    glEnd()
    glFlush()


"""draw_again restart the pygame window """


def draw_again():
    var0.set(False)  # off the var0 check button
    var1.set(False)  # off the var1 check button
    var2.set(False)  # off the var2 check button
    var3.set(False)  # off the var3 check button
    var4.set(False)  # off the var4 check button
    var5.set(False)  # off the var5 check button
    pygame.quit()  # close the current window
    init()  # initialize the window to be drawn
    while True:  # display the pygame window until the pygame quit function called
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()
        pygame.time.wait(10)
        window.update()  # update tkinter window


""" main display the pygame window with the specified mathematical function
"""


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


intro = Label(window, text="Welcome to my project", font=30, fg="teal")  # intro label text
choice = Label(window, text="choose functions", font=3, justify="center")  # a prompt label text

"""tkinter check buttons for each mathematical function  """
quadratic = Checkbutton(window, text=" X^2", variable=var0, onvalue=True, offvalue=False, bg="orange", width=5)
cubic = Checkbutton(window, text=" X^3", variable=var1, onvalue=True, offvalue=False, bg="orange", width=5)
sin = Checkbutton(window, text="sin(x)", variable=var2, onvalue=True, offvalue=False, bg="orange", width=5)
cosine = Checkbutton(window, text="cos(x)", variable=var3, onvalue=True, offvalue=False, bg="orange", width=5)
log = Checkbutton(window, text="log(x)", variable=var4, onvalue=True, offvalue=False, bg="orange", width=5)
exponential = Checkbutton(window, text=" 2^x", variable=var5, onvalue=True, offvalue=False, bg="orange", width=5)

# draw button and draw again button
draw_button = Button(window, text="Draw", bg='teal', command=main, width=8)
draw_again_button = Button(window, text="draw again", command=draw_again, bg="red")

# display labels, check buttons and buttons in grid
intro.grid(row=0, column=0, columnspan=3, padx=40, pady=20)
choice.grid(row=1, column=0, columnspan=3, padx=40, pady=20)
quadratic.grid(row=2, column=0, padx=10, pady=10)
cubic.grid(row=2, column=1, padx=10, pady=10)
sin.grid(row=2, column=2, padx=10, pady=10)
cosine.grid(row=3, column=0, padx=10, pady=10)
log.grid(row=3, column=1, padx=10, pady=10)
exponential.grid(row=3, column=2, padx=10, pady=10)
draw_button.grid(row=4, column=0, padx=10, pady=10)
draw_again_button.grid(row=4, column=1, padx=10, pady=10)

window.mainloop()
