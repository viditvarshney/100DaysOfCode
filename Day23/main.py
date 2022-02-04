import time
import turtle as t
from user import UserCar


myscreen = t.Screen()
myscreen.setup(height=600, width=600)
myscreen.tracer(0)

timmy = UserCar()
myscreen.listen()
myscreen.onkey(timmy.move(), "Up")


is_game_on = True

while is_game_on:
    time.sleep(0.1)
    myscreen.update()


myscreen.exitonclick()
