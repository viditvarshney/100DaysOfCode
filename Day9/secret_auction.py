import logo
import words
import os
import random
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo.logo)
time.sleep(2)
participants = {}

while True:
    clear()
    print(f"The item for bid is: {random.choice(words.things)}")
    user_name = input("enter you name: ")
    bid = int(input("enter you bid amount($): "))

    # dictionary to store data
    participants[user_name] = bid

    if(input("Anyone left?: 'yes' or 'no': ").casefold() == 'no'):

        break
key_tracker = ''
for key in participants:
    max_bid = 0

    if participants[key] > max_bid:
        max_bid = participants[key]
        key_tracker = key

print(f"The winner is {key_tracker[0]} for the highest bid of {max_bid}$.")
