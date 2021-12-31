import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
random_list = ['yellow', 'red', 'blue',
               'black', 'grey', 'orange', 'violet', 'cyan']

chosen_word = random.choice(random_list)

#  Displaying the blanks for the chossen word
lives_left = 6
display = ['_'] * len(chosen_word)
print(*display, end='\n \n')

while('_' in display):
    guess = input("Make a guess: ").lower()

    # if guessed letter is in the choosen word, then display it in 'display'

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives_left -= 1
        print(stages[lives_left])
        if lives_left == 0:

            break

    print(*display, end='\n \n')
if '_' not in display:
    print("You Won")
else:
    print("You Loose :-( ")
