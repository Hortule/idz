# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

def jhelp(hword):
    return {
        'питон': 'этот яп',
        'анаграмма': 'важный элемент этой игры',
        'простая': 'прилагательное характеризующее легкость этой игры',
        'сложная': 'прилагательное характеризующее трудность этой игры',
        'ответ': 'что ты пытаешься дать',
        'подстаканник': 'место для стакана'
        }[hword]
points = 2
# create a sequence of words to choose from
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)
guess = input("\nYour guess (if you need help write 'help'): ")
if 'help' in guess:
    points = 1
    print(jhelp(correct))
    guess = input('\nYour guess: ')
while guess != correct and guess != "":
    guess = input("\nYour guess (if you need help write 'help'): ")
    if 'help' in guess:
        points = 1
        print(jhelp(correct))
        guess = input('\nYour guess: ')
    
if guess == correct:
    print("That's it!  You guessed it!\n")

print("Thanks for playing.")
print('count of your points: ', points)
input("\n\nPress the enter key to exit.")
