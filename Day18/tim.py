"""Making Spirograph using Turtle"""

import random
import turtle as tu

tim = tu.Turtle()

tu.bgcolor('black')
tu.colormode(255)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(100):
    tim.color(random_color())

    tim.circle(100)
    tim.left(5)


my_screen = tu.Screen()

my_screen.exitonclick()
