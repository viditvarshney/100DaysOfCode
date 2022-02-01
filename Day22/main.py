#  PONG GAME

import turtle as t
from score import Score
from paddle import Paddle
from ball import Ball

myscreen = t.Screen()
myscreen.setup(width=800, height=600)
myscreen.bgcolor("black")
myscreen.title("PONG GAME")
# myscreen.tracer(0)

scoreboard = Score()

paddle_l = Paddle((-380, 0))
paddle_r = Paddle((380, 0))

ball = Ball()


myscreen.listen()
myscreen.onkey(paddle_r.move_up, "Up")
myscreen.onkey(paddle_r.move_down, "Down")
myscreen.onkey(paddle_l.move_up, "w")
myscreen.onkey(paddle_l.move_down, "s")


is_game_on = True
while is_game_on:
    # myscreen.update()
    ball.speed(1)
    ball.ball_move()


myscreen.exitonclick()
