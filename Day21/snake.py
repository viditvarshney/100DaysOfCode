import turtle as t
import time

my_screen = t.Screen()

X_POS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.createSnake()
        self.head = self.snake_segments[0]

    def createSnake(self):
        for x in X_POS:
            snake_body = t.Turtle(shape="circle")
            snake_body.color("white")
            snake_body.penup()
            snake_body.setx(x)
            self.snake_segments.append(snake_body)

    def move(self):

        for seg_no in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_no-1].xcor()
            new_y = self.snake_segments[seg_no-1].ycor()
            self.snake_segments[seg_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
