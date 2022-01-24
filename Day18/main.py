from random import choice, randint
import turtle as t

from numpy import angle

tim = t.Turtle()
t.screensize(10, 10)
#  Make a dotted Line.

# def dash():
#     space = 15

#     for _ in range(20):
#         tim.dot()
#         tim.penup()
#         tim.forward(space)
#         tim.pendown()


# for _ in range(4):
#     dash()
#     tim.right(90)

# Make a dashed line

# for _ in range(20):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


#  Make a overlapping geometry of shapes with a common base

# colors = ['gray', 'deep pink', 'gold', 'blue violet', 'lime', 'dark blue']

# for side_n in range(3, 9):

#     for _ in range(side_n):
#         tim.color(choice(colors))
#         tim.forward(150)
#         tim.right(360/side_n)

# ----------------------------------------------------

#  RANDOM WALK

# ----------------------------------------------------


#  RAndom Color Generation via RGB format
t.colormode(255)


# colors = ['gray', 'deep pink', 'gold', 'blue violet', 'lime', 'dark blue']


# east = 0    west = 1    north = 2    south = 3
angle = [0, 90, 180, 270]
tim.pensize(12)
tim.speed(0)


for _ in range(200):
    random_angle = choice(angle)
    tim.left(random_angle)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
   # generate random color
    tim.color((r, g, b))

    tim.forward(30)


my_screen = t.Screen()

my_screen.exitonclick()
