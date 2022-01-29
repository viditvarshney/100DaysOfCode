import turtle as t

tim = t.Turtle()
my_screen = t.Screen()
my_screen.listen()


def move_fw():
    tim.forward(20)


def move_bk():
    tim.bk(20)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pd()  # pendown


my_screen.onkey(key="w", fun=move_fw)
my_screen.onkey(key="s", fun=move_bk)
my_screen.onkey(key="a", fun=move_left)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="c", fun=clear)


my_screen.exitonclick()
