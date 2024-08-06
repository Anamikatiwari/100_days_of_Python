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
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#testing code
print(f"Pssst, the solution is: {chosen_word}.")

#TODO-1- Create an empty list called display. 
#For each letter in the chosen_word, add a "_" to 'display'. 
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess. 

guess = input("Guess a letter: ").lower()

#TODO-2- 


#day-7, vdo- 0