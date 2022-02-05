import random
import time
import turtle as t
from scoreboard import Score
from user import UserCar
from car import Car

myscreen = t.Screen()
myscreen.setup(height=600, width=600)
myscreen.tracer(0)

#  User Turtle
timmy = UserCar()
myscreen.listen()
myscreen.onkey(timmy.move, "Up")

# Cars on the road
car = Car()

# Scoreboard
scoreboard = Score()

# Game On Going
is_game_on = True

while is_game_on:
    time.sleep(0.1)
    if timmy.ycor() > 280:
        scoreboard.update_score()
        timmy.timmy_reset()

    # Car moving from left --> right
    car.move_car()
    myscreen.update()


myscreen.exitonclick()
