from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", False,
                   align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False,
                   align='center', font=('Arial', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"G A M E  O V E R", False,
                   align='center', font=('Arial', 20, 'bold'))
