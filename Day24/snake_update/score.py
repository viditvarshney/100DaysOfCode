import time
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        previous_high_score = open(
            ".\Day24\snake_update\previous_high_score.txt", mode="r").read()
        self.highScore = int(previous_high_score)
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.highScore}", False,
                   align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()

        if self.score > self.highScore:
            self.highScore = self.score
        self.write(f"Score: {self.score} High Score: {self.highScore}", False,
                   align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"G A M E  O V E R", False,
    #                align=HIGHSCORE_ALIGNMENT, font=FONT)

    def restarting_game(self):

        self.goto(0, 0)
        self.write(f"Game Restarting...", False,
                   align=ALIGNMENT, font=FONT)

        time.sleep(1)

        self.goto(0, 260)

    def write_highscore(self):
        with open(".\Day24\snake_update\previous_high_score.txt", mode="w") as file:
            file.write(str(self.highScore))
