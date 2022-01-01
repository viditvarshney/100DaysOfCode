import random
import stages
import words


chosen_word = random.choice(words.random_word_list)
print(stages.logo)

#  Displaying the blanks for the chossen word
lives_left = 6
display = ['_'] * len(chosen_word)

print(*display, end='\n \n')

while('_' in display):
    guess = input("Make a guess: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    # if guessed letter is in the choosen word, then display it in 'display'

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(
            f"\nYour guessed letter: {guess} is not in the chosen word. You lost one life.")
        lives_left -= 1
        print(stages.stages[lives_left])
        if lives_left == 0:

            break

    print(*display, end='\n \n')
if '_' not in display:
    print("You Won")
else:
    print("You Loose :-( ")
