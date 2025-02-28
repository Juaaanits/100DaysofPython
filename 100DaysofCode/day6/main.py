import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3
import os

clear = lambda: os.system('cls')

randomWord = random.choice(word_list)
characterArray = list(randomWord)
wordLength = len(randomWord)

lives = 6
end_of_game = False  # If game is over or not

print(logo3)
print('\nTo win, guess the word before the person is hung.\n')

display = []
wrong_guesses = []

# For displaying blank lines
for _ in range(wordLength):
    display += "_"

while not end_of_game:
    letter = input("Guess a letter: ").lower()
    clear()

    # If letter was already guessed incorrectly
    if letter in wrong_guesses:
        print(f"You've already guessed '{letter}'. Pick another.\n")
        continue  # Ask the user for a new letter without losing a life

    # If the letter is not in the word (wrong guess)
    if letter not in characterArray:
        wrong_guesses.append(letter)  # Store wrong guesses
        print(f"Wrong guesses: {', '.join(wrong_guesses)}") 
        print(f"{' '.join(display)}\n")
        print(stages[lives])
        print(f"\nYou guessed '{letter}', which is not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was '{randomWord}'")

    else:
        # If the letter is in the word, update display
        for position in range(wordLength):
            if randomWord[position] == letter:
                display[position] = letter

        print(f"{' '.join(display)}\n")

    # Check if player has won
    if "_" not in display:
        end_of_game = True
        print("You win!")
        print(f"The word was '{randomWord}'")
