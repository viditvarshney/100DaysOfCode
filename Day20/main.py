import time
import turtle as t
from snake import Snake


my_screen = t.Screen()
my_screen.bgcolor("blue")
my_screen.setup(height=600, width=600)

my_screen.tracer(0)
# # Create Snake body

snaky = Snake()
my_screen.listen()
# Snake Moving

is_snake_moving = True
while is_snake_moving:
    my_screen.update()
    time.sleep(0.1)
    snaky.move()

    my_screen.onkey(key="Left", fun=snaky.move_left)
    my_screen.onkey(key="Up", fun=snaky.move_up)
    my_screen.onkey(key="Down", fun=snaky.move_down)
    my_screen.onkey(key="Right", fun=snaky.move_right)


my_screen.exitonclick()
