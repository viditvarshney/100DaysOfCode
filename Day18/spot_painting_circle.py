import turtle as tt
import random

tim = tt.Turtle()


my_screen = tt.Screen()

tt.colormode(255)
# Take the turtle to the starting point

tim.hideturtle()
tim.penup()
tim.goto(-100, -300)
tim.pendown()


# Generate random RGB color

tim.speed(0)


def random_Color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

# make the turtle invisible whil going to new position


def invisible():
    tim.left(90)
    tim.pu()
    tim.forward(40)
    tim.right(90)
    tim.pd()

# making circles


def making_circle(radius):
    tim.color(random_Color())

    tim.circle(radius)

# making concentric circles


for rad in range(280, 20, -40):
    making_circle(rad)
    tim.dot(20)
    invisible()


my_screen.exitonclick()
