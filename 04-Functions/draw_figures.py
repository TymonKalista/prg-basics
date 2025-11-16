import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

figures.draw_reectangle(50,100)
pen.penup()
pen.goto(100,100)
pen.pendown()

figures.draw_reectangle(100,50)

figures.draw_square(50)

figures.draw_triangle(70)


# Hide the turtle and finish
pen.hideturtle()
window.mainloop()