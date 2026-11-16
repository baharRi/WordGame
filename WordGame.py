#The original game was made in Python and transformed into JS for added GUI. This is the original. 

import random

#game setup
game_name = "word raider"
word_bank = []

with open("words.txt") as word_file: 
    for word in word_file:
        word_bank.append(word.rstrip().lower())

selected_word = random.choice(word_bank)

#game behavior
MAX_TURNS = 6

misplaced_letters = set()
incorrect_letters = set()
used_turns = 0

print(f"Welcome to {game_name}!")
print(f"You have {MAX_TURNS} turns to guess the word.")

#main game loop
while used_turns < MAX_TURNS: 
    guess = input("Type a word to guess (or type 'stop' to end the game):").lower().strip()
    
    if guess == "stop":
        break
    if len(guess) == 5 and guess in word_bank:
        used_turns +=1
        for i, letter in enumerate(guess):
            if letter == selected_word[i]:
                print(letter, end=' ')
            elif letter in selected_word:
                print("_", end=' ')
                misplaced_letters.add(letter)
            else: 
                print("_", end=' ')
                incorrect_letters.add(letter)
        print(misplaced_letters)

        #win condition
        if guess == selected_word:
            print("Congratulations! You guessed the word.")
            break

    else: 
        print("Please enter a valid 5 letter word.")

print(f"The word was {selected_word}.")