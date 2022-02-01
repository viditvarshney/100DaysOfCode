from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 40, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 245)
        self.write(f"{self.l_score} | {self.r_score}", False,
                   align=ALIGNMENT, font=FONT)

    def update_lscore(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", False,
                   align=ALIGNMENT, font=FONT)

    def update_rscore(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", False,
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"G A M E  O V E R", False,
                   align='center', font=('Arial', 20, 'bold'))
