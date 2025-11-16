# Draw a square
import turtle
pen = turtle.Turtle()

def draw_square(x):
    for i in range(4):
        pen.forward(x)
        pen.right(90)


def draw_triangle(y):
    for i in range(3):
        pen.forward(y)
        pen.right(120)

def draw_reectangle(x,y):
    for i in range(2):
        pen.forward(x)
        pen.right(90)
        pen.forward(y)
        pen.right(90)