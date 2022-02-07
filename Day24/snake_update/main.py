from concurrent.futures.process import _sendback_result
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
        snaky.snake_extention()

    # Detect Collison with Walls

    if snaky.head.xcor() > 290 or snaky.head.xcor() < -290 or snaky.head.ycor() > 290 or snaky.head.ycor() < -290:
        # scoreboard.game_over()
        scoreboard.score = 0
        snaky.reset_snake()
        scoreboard.restarting_game()
        time.sleep(1)

    #  Detech Tail Collison: When head collides with any segment of snake

    for any_segment in snaky.snake_segments[1:]:

        if snaky.head.distance(any_segment) < 9:
            # scoreboard.game_over()
            scoreboard.score = 0

            scoreboard.restarting_game()

            snaky.reset_snake()


my_screen.exitonclick()
