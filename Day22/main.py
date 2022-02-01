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

    # Detect collision with  walls (walls on y -axis)

    if ball.ycor() > 285 or ball.ycor() < -285:

        ball.bounce_y()

    # Detect colllision of ball with paddle
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 350) or (ball.distance(paddle_l) < 50 and ball.xcor() < -350):
        print("collided")
        ball.bounce_x()


myscreen.exitonclick()
