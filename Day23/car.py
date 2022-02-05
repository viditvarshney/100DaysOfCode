
from turtle import Turtle
import random

MOVE_DISTANCE = 15
COLORS = ['gray', 'deep pink', 'gold', 'blue violet', 'lime', 'dark blue']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.car_models = []
        self.createCars()

    def createCars(self):
        for _ in range(10):
            next_car = Turtle()

            next_car.pu()
            next_car.left(180)
            next_car.shape("square")
            next_car.shapesize(stretch_len=1.3, stretch_wid=1)
            next_car.color(random.choice(COLORS))

            next_car.goto(310, self.random_car_start_pos())
            self.car_models.append(next_car)

        print(self.car_models)

    def random_move_steps(self):
        return random.randint(0, 10)

    def random_car_start_pos(self):
        return random.randint(-250, 250)

    def move_car(self):
        self.speed(1)
        for car in self.car_models:
            if car.xcor() < -310:
                car.goto(310, self.random_car_start_pos())
            car.forward(self.random_move_steps())
