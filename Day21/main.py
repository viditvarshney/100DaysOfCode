import time
import turtle as t
from snake import Snake
from food import Food
from score import Score


my_screen = t.Screen()
# Score Board

scoreboard = Score()

my_screen.bgcolor('black')
my_screen.setup(height=600, width=600)

my_screen.tracer(0)
# # Create Snake body

snaky = Snake()
food = Food()
my_screen.listen()
my_screen.onkey(key="Left", fun=snaky.move_left)
my_screen.onkey(key="Up", fun=snaky.move_up)
my_screen.onkey(key="Down", fun=snaky.move_down)
my_screen.onkey(key="Right", fun=snaky.move_right)
# Snake Moving

is_snake_moving = True
while is_snake_moving:
    my_screen.update()
    time.sleep(0.1)
    snaky.move()

    # Detec Collison of Snake With Food

    if snaky.head.distance(food) < 15:

        scoreboard.update_score()
        food.reset_food()


my_screen.exitonclick()