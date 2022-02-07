
from turtle import Turtle
import random


COLORS = ['gray', 'deep pink', 'gold', 'blue violet', 'lime', 'dark blue']


class Car:
    def __init__(self):
        self.car_models = []
        self.move_distance = 5

    def createCar(self):
        # To reduce the car frequency
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            next_car = Turtle("square")
            next_car.shapesize(stretch_wid=1, stretch_len=2)
            next_car.pu()
            next_car.color(random.choice(COLORS))

            next_car.goto(310, self.random_y())
            self.car_models.append(next_car)
            # print(self.car_models)
            # self.move_car()  It can't be here because after appending one car to the 'car_models' it will stuck in the
            # for loop of 'move_car()' function.
            # self.move_car()

    def random_y(self):
        return random.randint(-250, 250)

    def move_car(self):
        for car in self.car_models:
            car.backward(self.move_distance)
