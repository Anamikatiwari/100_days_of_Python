#step-1
word_list = ["ardvark", "baboon", "camel"]

#TODO-1- Randomly choose a word from the word_list and assign it to a variable called choosen_word. 
#TODO-2- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. 
#TODO-3-Check if the leter the user guessed(guess) is one of the letters in the choosen_word.


#challenge-1 
#TODO-1- Randomly choose a word from the word_list and assign it to a variable called choosen_word. 
import random
chosen_word = random.choice(word_list)

#TODO-2- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. 
guess = input("Guess a letter: ").lower()

#TODO-3-Check if the leter the user guessed(guess) is one of the letters in the choosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


#--------------------------------------------------------------------------------------------------

#step-2
#challenge-2

import random