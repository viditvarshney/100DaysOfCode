import turtle as tt
import random

tim = tt.Turtle()


my_screen = tt.Screen()

tt.colormode(255)
# Take the turtle to the starting point

tim.hideturtle()
tim.penup()
tim.goto(-200, -200)
tim.pendown()

# Generate random RGB color

tim.speed(0)


def random_Color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def invisible_dots():

    tim.left(90)
    tim.penup()
    tim.forward(40)
    tim.left(90)
    tim.forward(400)
    tim.pendown()
    tim.right(180)


def making_dots():
    for _ in range(10):
        tim.dot(20, random_Color())
        tim.penup()
        tim.forward(40)
        tim.pendown()


making_dots()
for _ in range(10):
    invisible_dots()
    making_dots()


my_screen.exitonclick()
