import logo
from random import randint
import time


# Easy diff function
random_digit = randint(1, 100)


def game(attempts):

    while attempts > 0:
        choice = int(input("Make a choice: "))
        if choice == random_digit:
            print("*******************************\n")

            print(f"That's CORRECT, Number choosen was {random_digit}\n")

            print("*******************************")

            break
        else:
            if choice > random_digit:
                print("You guessed too High, Try Again.")
            else:
                print("You guessed too Low, Try Again.")
            attempts -= 1
            print(f"You have {attempts} attempts to guess the correct number.")
    if attempts == 0:
        print("*******************************\n")

        print(f"GAME OVER, The number was {random_digit}.\n")

        print("*******************************")


while True:

    print(logo.logo)
    print('\n')
    print("Welcome to Guess the Number Game. ")
    time.sleep(2)

    print("I have choosen the word between 1 & 100, You need to guess it correctly.")
    print(f"testing Code: {random_digit}")
    time.sleep(1)
    difficulty = input("Choose the difficulty: 'easy' or 'hard': ")

    if difficulty.casefold() == 'easy':
        print("You have 10 attempts to guess the correct number.")
        game(attempts=10)
    elif difficulty.casefold() == 'hard':
        print("You have 5 attempts to guess the correct number.")
        game(attempts=5)
    else:
        print("Invalid Difficulty selection")
    if(input("Want to play AGAIN? 'y' or 'n': ").casefold() == 'n'):
        print("Ok Bye, Hope we shall meet soon")
        break
