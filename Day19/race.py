import turtle as t
import random


# screen

my_screen = t.Screen()

# canvas height and weight
my_screen.setup(width=500, height=500)

# CApturing the user input in a variable
user_bet = my_screen.textinput(
    title="Make your bet.", prompt="Which turtle will win the race? Enter the color: 'gray, deep pink, gold, blue violet, lime, dark blue'")


# color state of eachg turtle

colors = ['gray', 'deep pink', 'gold', 'blue violet', 'lime', 'dark blue']


y_pos = [-100, -50, 0, 50, 100, 150]
turtles = []

for i in range(6):

    next_turtle = t.Turtle(shape="turtle")
    next_turtle.color(colors[i])
    next_turtle.pu()
    next_turtle.goto(x=-230, y=y_pos[i])
    turtles.append(next_turtle)


# radomly move forward


def random_steps():
    return random.randint(1, 20)


# Game

is_race = False

if user_bet:
    is_race = True

while is_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You Won!, The {winner_color} turtle is the Winner.")

            else:
                print(f"You Lost!, The {winner_color} turtle is the Winner.")

        # random_distance = random.randint(0, 10)
        turtle.forward(random_steps())


my_screen.exitonclick()
