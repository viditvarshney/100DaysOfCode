import random
import time
print("\n\nWelcome..\n")
time.sleep(2)
print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print("\n\n RULES\n")
print('''
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.\n''')
# d = {0: 'rock', 1: 'paper', 2: 'scissor'}

while True:
    while True:
        my_turn = int(
            input("Choose one among 0: rock, 1: paper or 2: scissor? "))
        if my_turn == 0 or my_turn == 1 or my_turn == 2:
            break
        else:
            print("Invalid input.")
            continue

    computer_turn = random.randint(0, 2)

    win_dict = {
        0: "SCISSORS",
        1: "PAPER",
        2: "ROCK",
    }
    my_win_option = win_dict[my_turn]
    if my_turn == computer_turn:
        print("It's a draw..")
    elif my_turn == my_win_option:
        print("You wins")
    else:
        print("Computer Wins")

    if input("New Game? ('Yes') or ('No'): ").casefold() == 'no':
        break
