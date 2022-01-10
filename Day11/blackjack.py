import random
import logo

# Cards Numbers
# Ace is 11, J,K,Q (each value is 10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def Score(cards):
    """Returns the total score after checking blackjack or sum greater than 21"""

    # check for a blackjack (a hand with only 2 cards: ace + 10)
    #  and return 0 instead of the actual score. 0 will represent a blackjack in the game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    #  check for 11  in the list,

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        # print("Your score exceeds 21 so '11' is replaced by '1'.")
    return sum(cards)


# generates a new random card from the list


def rand_generator():
    """Draws a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "It's a draw"
    elif user_Score == 0:
        return "You Won with BLACKJACK"
    elif dealer_Score == 0:
        return "You lose! Dealer has the BLACKJACK"
    elif user_Score > 21 or (user_Score > 21 and dealer_Score > 21):
        return "You Lose! You went over 21"
    elif dealer_Score > 21:
        return "You Won, Dealer went over 21"
    elif user_Score > dealer_Score:
        return "You Win..."
    else:
        return "You lose..."
# random two caards for user and dealer


while True:
    print(logo.logo)
    player = []
    dealer = []

    game_over = False

    for _ in range(2):
        player.append(rand_generator())
        dealer.append(rand_generator())

    while not game_over:

        user_Score = Score(player)
        dealer_Score = Score(dealer)
        game_over = False

        print(f"Your cards: {player}, and score: {user_Score}\n")
        print(f"dealer cards: {dealer[0]}\n")

        if user_Score == 0 or dealer_Score == 0 or sum(player) > 21:
            game_over = True
        else:
            if input("You want a HIT? 'y' or 'n' for stand: ").casefold() == 'y':
                player.append(rand_generator())
                # print(player)

            else:

                game_over = True

        while dealer_Score > 0 and dealer_Score < 17:
            dealer.append(rand_generator())
            dealer_Score = Score(dealer)
    print(f"   Your final hand: {player}, final score: {user_Score}\n")
    print(
        f"   Computer's final hand: {dealer}, final score: {dealer_Score}\n")

    print("*******************************************\n")
    print(f"\t{compare(user_Score, dealer_Score)}\n")
    print("*******************************************")

    if(input("Want to play again? 'y' or 'n': ").casefold() == 'n'):
        print("Ok, Bye..... Game Ended!!!")
        break
