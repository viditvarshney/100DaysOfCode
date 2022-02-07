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
car_manager = Car()

# Scoreboard
scoreboard = Score()

# Game On Going
is_game_on = True

while is_game_on:
    time.sleep(0.1)
    myscreen.update()
    if timmy.ycor() > 280:
        scoreboard.update_score()
        car_manager.move_distance += 0.1
        timmy.timmy_reset()

    # Car moving from left --> right

    car_manager.createCar()
    car_manager.move_car()

    # detect collision of turtle with any car
    for car in car_manager.car_models:

        if timmy.distance(car) < 20:
            scoreboard.game_over()
            is_game_on = False


myscreen.exitonclick()
