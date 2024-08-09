from random import randint

#Global constant
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer. 
def check_answer(guess, answer):
    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    else:
        print("You got it! The answer was (answer).")



# Make function to set difficulty. 
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS
        

#Let the user guess a number. 
guess = int(input("Make a guess:"))




#Track the number of turns and reduce by 1 if they get it wrong.

#Repeat the guessing functionality if they get it wrong.

  