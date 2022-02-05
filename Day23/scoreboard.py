from turtle import Turtle

ALIGNMENT = "left"
FONT = ('Courier', 20, 'bold')


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.pu()
        self.goto(-260, 260)
        self.write(f"Level: {self.score}", False,
                   align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", False,
                   align=ALIGNMENT, font=('Arial', 20, 'bold'))
