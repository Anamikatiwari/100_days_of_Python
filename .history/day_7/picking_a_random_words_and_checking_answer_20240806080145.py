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

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)
guess = input("Guess a letter: ").lower()

#TODO-2-  Loop through each position in the chosen_word; 
#If the letter at that position matches 'guess' then reveal that letter in the display at thet position. 
#e.g; If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]. 
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    
        
        
#TODO-3- Print 'display ' and you should see the guessed letter in the correct position and every other letter replace with "_". 
print(display)

#--------------------------------------------------------------------------------------------------------------------------------------------

#step-3
#challenge-3

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#testing code
print(f"Pssst, the solution is: {chosen_word}.")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
    
#TODO-1- Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won. 

guess = input("Guess a letter: ").lower()

#Check guessed letter
for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
    if letter == guess:
        

    

