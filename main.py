import numpy as np
import pandas as pd
import random


def get_list_of_words(input_file):
    list = []
    with open(input_file) as file:
        for line in file:
            list.append(line.strip())
    return list


def play_wordle():
    list_of_words = get_list_of_words("wordle-answers-alphabetical.txt")
    target_word = random.choice(list_of_words).upper()
    print("Target word: " + target_word)
    print(list(target_word))
    print()
    none_list = [None, None, None, None, None]
    guess_history = {"Guess 1": none_list, "Guess 2": none_list, "Guess 3": none_list,
                     "Guess 4": none_list, "Guess 5": none_list, "Guess 6": none_list}

    guess_count = 0
    while guess_count < 6:

        guess_count = guess_count + 1
        print("Guess: " + str(guess_count))
        inputFromUser = get_input(list_of_words)

        if guess_count == 6:
            print("Guess count: " + str(guess_count))
            guess_history["Guess " + str(guess_count)] = inputFromUser
            print(generate_df(guess_history))
            break
        else:

            # first check
            # if the input guess is correct
            if inputFromUser == list(target_word):
                print("Correct guess")
                guess_history["Guess " + str(guess_count)] = inputFromUser
                print(generate_df(guess_history))
                guess_count = 6
            elif inputFromUser in guess_history.values():
                print(''.join(inputFromUser))
                print("word already used")
                guess_count = guess_count - 1
            else:
                print("(partially) incorrect guess")
                guess_history["Guess " + str(guess_count)] = inputFromUser
                print(generate_df(guess_history))


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
    df = pd.DataFrame(data=my_dict).transpose()
    return df


play_wordle()
