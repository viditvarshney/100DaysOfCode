import time
import data
import logo
import random

# generatew random account from the data.py


def randomChoice():
    return random.choice(data.data)

# format the data


def format(acc):
    name = acc['name']
    des = acc['description']
    country = acc['country']

    return f"{name},{des}, from {country}."

# check who has more followers against users input


def compare(guess, a_follower, b_follower):

    if (a_follower > b_follower and guess == 'a') or (a_follower < b_follower and guess == 'b'):
        return True
    elif (a_follower > b_follower and guess == 'b') or (a_follower < b_follower and guess == 'a'):
        return False


def game():
    score = 0
    print(logo.logo)
    time.sleep(2)
    B = randomChoice()

    while True:
        A = B
        B = randomChoice()
        while A == B:
            B = randomChoice()
        print(f"Compare A: {format(A)}")
        print(logo.vs)
        print(f"With B: {format(B)}")

        guess = input("'Who has more follower?' Choose A or B: ").lower()

        result = compare(guess, A['follower_count'], B['follower_count'])

        if result:
            score += 1
            print("*******************************\n")

            print(f"You Guessed Right, You Current Score: {score}.\n")

            print("*******************************")

        else:
            print("*******************************\n")

            print(f"Oh! That's Wrong, Your final score is {score}.\n")
            print("*******************************")
            if input("Want to play again? 'y' or 'n': ").casefold() == 'y':
                time.sleep(1)
                print("Ok!, Refreshing gaming stats...")
                time.sleep(3)
                game()
            else:
                time.sleep(2)
                print("Closing The current session...")
                time.sleep(2)
                print("OK, Have a nice day.")
                break
    return


game()
