# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import random


# import Numpy as np


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def get_list_of_words(input_file):
    list = []
    with open(input_file) as file:
        for line in file:
            list.append(line.strip())
    return list


def play_wordle():
    list_of_words = get_list_of_words("wordle-answers-alphabetical.txt")
    target_word = random.choice(list_of_words)
    none_list = [None, None, None, None, None]
    guess_history = {"Guess 1": none_list, "Guess 2": none_list, "Guess 3": none_list,
                     "Guess 4": none_list, "Guess 5": none_list, "Guess 6": none_list}

    inputFromUser = get_input(list_of_words)
    print(inputFromUser)

    guess_history["Guess 1"] = inputFromUser
    print("Target word: " + target_word)
    print(generate_df(guess_history))
    # print(df)


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


def loop():
    for i in range(0, 6):
        print(i)

    print("hello world")

play_wordle()
loop()