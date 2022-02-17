import turtle as t
import pandas as pd
import time

my_screen = t.Screen()
my_screen.setup(600, 700)
my_screen.title("NAME ALL THE STATE NAMES")

my_screen.bgpic("./india_map.gif")

# scoreboard tracking
scoreboard = t.Turtle()
scoreboard.hideturtle()
scoreboard.pu()
scoreboard.goto(0, 300)
scoreboard.pd()

# Track the number of states / 28 in the upper most space -- Done


data = pd.read_csv("./states_cor.csv")
data_list = data.values.tolist()
states = data.state.tolist()
correct_states_sofar = 0
attempts = 0
# scoreboard.write(f"Score: {correct_states_sofar}/28 in {attempts} attempts", False,
#                  align="center", font=('Courier', 15, 'bold'))

already_named = []  # list to track already named states

while correct_states_sofar < 28:

    # Take input from the user

    user_guess = my_screen.textinput(
        f"Score: {correct_states_sofar}/ 28 in {attempts} attempts", "Name the another state: ").title()

    if user_guess == "Exit":
        break

    # check if user_guess is already named

    if user_guess in already_named:
        t.color("red")
        t.write(f"State Already Named", False,
                align="center", font=('Courier', 20, 'bold'))
        t.hideturtle()
        time.sleep(2)
        t.clear()
    else:
        if user_guess in states:
            # add the named states to a new list
            already_named.append(user_guess)

            correct_states_sofar += 1
            choosen_state_ind = states.index(user_guess)
            # print(data_list[choosen_state_ind])

            # locate the named state on the map

            state_locator = t.Turtle("circle")

            state_locator.shapesize(stretch_len=0.3, stretch_wid=0.3)
            state_locator.pu()
            choosen_state_row = data_list[choosen_state_ind]
            state_locator.goto(x=choosen_state_row[1],
                               y=choosen_state_row[2])
            state_locator.pd()
            state_locator.color("red")
            state_locator.write(f"{choosen_state_row[0]}", False,
                                align="center", font=('Courier', 8, 'bold'))

        else:
            # alert when the state is not present
            t.color("red")
            t.write(f"State Not Found", False,
                    align="center", font=('Courier', 20, 'bold'))
            t.hideturtle()
            time.sleep(2)
            t.clear()
    attempts += 1
    scoreboard.clear()
    scoreboard.write(f"Score: {correct_states_sofar}/28 in {attempts} attempts", False,
                     align="center", font=('Courier', 15, 'bold'))

# Create a csv file when user exit the game: contain the remaining states

remaining_states = pd.DataFrame(
    set(data.state) - set(already_named))
remaining_states.to_csv("./learn.csv")


# my_screen.mainloop()  # It is the alternative to exitonClick()
