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

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

#---------------------------------------------------------------------------------------

#step-4
#challenge-4
import random

stages = ['''
+----+
 |    |
 O    |
/|\   |
 /\   |
      |
=======
''', ''''
+----+
 |    |
 O    |
/|\   |
 /    |
      |
=======
''', ''''
+----+
 |    |
 O    |
/|\   |
      |
      |
=======
''', ''''
+----+
 |    |
 O    |
/|    |
      |
      |
=======
''', ''''
+----+
 |    |
 O    |
/     |
      |
      |
=======
''', ''''
+----+
 |    |
 O    |
      |
      |
      |
=======
''', ''''
+----+
 |    |
      |
      |
      |
      |
=======

''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1- Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6. 
lives = 6

#testing code
print(f"Pssst, the solution is: {chosen_word}.")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
    
#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
       
       
#TODO-2- If guess is not a letter in the chosen_word,
#Then recude 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You Lose."

if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose.")
    

#Join all the element in the list and turn it into string. 
print(f"{' '.join(display)}") 

#Check if user has got all letters. 
if "_" not in display:
    end_of_game = True
    print("You win.")
    

#TODO-3- Print the ASCII art from 'stsges' that corresponds to the current number of 'lives' the user has remaining. 

print(stages[lives])


#-------------------------------------------------------------------------------------------------------------------------------

#step-5
#challenge-5

import random

#TODO-1- Update the word list to use  hangman_words.py 
#Delete this line: Word_list = ["ardvark", "baboon", "camel"]

chosen_word =  random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives =6

#TODO-3- Import the loop from hangman_art.py it at the stsrt of game. 
 
#testing code
print(f'pssst, the solution is ')
