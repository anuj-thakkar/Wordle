import numpy as np
import pandas as pd
import random
from termcolor.termcolor import colored

TILES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect': '⬛'
}


def validate_guess(guess, answer):
    guessed = []
    tile_pattern = []
    # Loop through every letter of the guess
    for i, letter in enumerate(guess):
        # If the letter is in the correct spot, color it in green and add the green tile
        if answer[i] == guess[i]:
            guessed += colored(letter, 'green')
            tile_pattern.append(TILES['correct_place'])
            # Replace the existing letter in the answer with -
            answer = answer.replace(letter, '-', 1)
        # whereas if the letter is in the correct spot, color it in yellow and add the yellow tile
        elif letter in answer:
            guessed += colored(letter, 'yellow')
            tile_pattern.append(TILES['correct_letter'])
            # Replace the existing letter in the answer with -
            answer = answer.replace(letter, '-', 1)
        # Otherwise, the letter doens't exist, just add the grey tile
        else:
            guessed += letter
            tile_pattern.append(TILES['incorrect'])

    # Return the joined colored letters and tiles pattern
    return ''.join(guessed), ''.join(tile_pattern)


def get_list_of_words(input_file):
    list = []
    with open(input_file) as file:
        for line in file:
            list.append(line.strip())
    return list


def play_wordle():
    history_guesses = []
    tiles_patterns = []
    colored_guessed = []

    list_of_words = get_list_of_words("wordle-answers-alphabetical.txt")
    target_word = random.choice(list_of_words).upper()
    print("Target word: " + target_word)
    print()
    none_list = [None, None, None, None, None]
    guess_history = {"Guess 1": none_list, "Guess 2": none_list, "Guess 3": none_list,
                     "Guess 4": none_list, "Guess 5": none_list, "Guess 6": none_list}

    isGameWon = False

    guess_count = 0
    while guess_count < 6:

        guess_count = guess_count + 1
        print("Guess: " + str(guess_count))
        inputFromUser = get_input(list_of_words)  # type <list>

        color_map(inputFromUser, history_guesses, target_word, colored_guessed, tiles_patterns)

        if guess_count == 6:

            if inputFromUser == list(target_word):
                isGameWon = True

            guess_history["Guess " + str(guess_count)] = inputFromUser
            print(generate_df(guess_history))

            if isGameWon:
                print()
                print("Congrats! You won in " + str(guess_count) + " attempts")
            else:
                print()
                print("You used all 6 attempts. Try again!")
        else:

            # first check
            # if the input guess is correct
            if inputFromUser == list(target_word):
                print("Congrats! You won in " + str(guess_count) + " attempt(s)")
                guess_history["Guess " + str(guess_count)] = inputFromUser
                print(generate_df(guess_history))
                print()
                guess_count = 6
            elif inputFromUser in guess_history.values():
                print(''.join(inputFromUser))
                print("word already used")
                guess_count = guess_count - 1
            else:

                print()
                print("(Partially) incorrect guess")
                guess_history["Guess " + str(guess_count)] = inputFromUser
                print(generate_df(guess_history))

                print()


# returns a list
def get_input(list_of_words):
    isValidInput = False

    while not isValidInput:
        response = input("Enter a 5-letter Word :")
        if len(response) != 5:
            print('Word needs to be exactly 5 letters')
        elif response not in list_of_words and len(response) == 5:
            print('Not a word')
        else:
            return list(response.upper())


def generate_df(my_dict):
    print("### GUESS HISTORY ###")
    df = pd.DataFrame(data=my_dict).transpose()
    return df

def color_map(inputFromUser, history_guesses, target_word, colored_guessed, tiles_patterns):
    guess = ''.join(inputFromUser).upper()

    # Append the valid guess
    history_guesses.append(guess)
    # Validate the guess
    guessed, pattern = validate_guess(guess, target_word)
    # Append the results
    colored_guessed.append(guessed)
    tiles_patterns.append(pattern)

    # For each result (also the previous ones), it'll print the colored guesses and the tile pattern
    for g, p in zip(colored_guessed, tiles_patterns):
        print(g, end=' ')
        print(p)
    print()

play_wordle()
