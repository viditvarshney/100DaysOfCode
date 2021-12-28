import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the world of Adventure\n")
time.sleep(2)
print("You mission is to find the most dangerous treasure\n")


def adGame():
    time.sleep(2)

    print("You approached trijunction:\n")
    time.sleep(2)
    userChoice1 = input("Select left or right to proceed in the game.")

    if (userChoice1.casefold() == 'left'):
        userChoice2 = input(
            "You arrived on the very old temple, Want to go inside alone or search for any person outside? Inside or Search: ")
        if(userChoice2.casefold() == 'inside'):
            print("You entered in the temple, You found an old book with map. It may be the map of the treasure but may be a trap.")
            userChoice3 = input("Want to follow the map?: Yes or No: ")
            if(userChoice3.casefold() == 'No'):
                print(
                    "Good Decision, Map cab be a Trap, Better would be I will read this book. ")
                userChoice4 = input("Enter 'READ' to read the book: ")
                if(userChoice4.casefold() == 'READ'):
                    print(
                        "After Reading the book, You gained the knowledge of most of the danger, Now You came very close the treasure.")
                    print("Choose Wisely: Its a point of treasure or death: ")
                    userChoice5 = input("What would be the sum of '5' + '5': ")
                    if(userChoice5 == '55'):
                        print(
                            "Hurray! You found the treasure that was a mystry till today. ")
                        time.sleep(2)
                        print("YOU WON")
                        time.sleep(2)
                        print("You found the treaure of worth over 100Cr")
                    else:
                        print("No, Thats not right, You have to die......")
                        time.sleep(2)
                        print("An stream of arrows killed you.!!")
                        time.sleep(2)
                        print("GAME OVER")

                else:
                    print("GAME OVER")

            else:
                print("By following the map, You came to cave od Lion\n")
                time.sleep(2)
                print("You were killed. \n")
                time.sleep(2)
                print("GAME OVER")

        else:
            print("You waited outside, and maneater came and he killed you.\n")
            time.sleep(2)
            print("GAME OVER")

    else:
        print("WRONG TURN ")
        time.sleep(1)
        print("GAME OVER")


playAgain = 'yes'


while playAgain.casefold() == 'yes' or playAgain.casefold() == 'y':

    adGame()
    playAgain = input(
        "Do you want to play again? (enter 'yes' or 'y' for continue playing: ")
