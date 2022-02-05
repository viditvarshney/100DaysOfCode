from turtle import Turtle
TURTLE_START_POSITION = (0, -280)


class UserCar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.pu()
        self.goto(TURTLE_START_POSITION)

        # self.move()

    def move(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def timmy_reset(self):
        self.goto(TURTLE_START_POSITION)
