import random

# Cards Numbers
# Ace is 11, J,K,Q (each value is 10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
dealer = []

rand_n1 = player.append(random.choice(cards))
rand_n2 = player.append(random.choice(cards))

dealer_rand1 = dealer.append(random.choice(cards))


def isAce(random_cards_list):
    if 11 in random_cards_list:
        return True
    else:
        return False


def is10(random_cards_list):
    if 10 in random_cards_list:
        return True
    else:
        return False


def isBlackJack(player_list):
    if isAce(player_list) == True and is10(player_list) == True:
        return True
    else:
        return False
# check if player got the blackjack? If yes : player wins


if isBlackJack(player):
    print("You wins as u have blackjack.")
