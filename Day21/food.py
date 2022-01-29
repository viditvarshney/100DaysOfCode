from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.speed(0)
        self.reset_food()

    def reset_food(self):
        colors = ['gray', 'deep pink', 'gold',
                  'blue violet', 'lime', 'dark blue']
        shapes = ["square", "circle", "triangle"]
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))
        self.shapesize(stretch_len=0.65, stretch_wid=0.65)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 250)
        self.pu()
        self.goto(random_x, random_y)
