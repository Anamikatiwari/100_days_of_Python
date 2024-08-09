from random import randint

#Global constant
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Function to check user's guess against actual answer. 
def check_answer(guess, answer, turns):
    """ Checks answer against   """
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print("You got it! The answer was (answer).")


# Make function to set difficulty. 
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        

def game():
    # Choosing a random number between 1 and 100. 
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaning to guess the number.")

    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        #Let the user guess a number. 
        guess = int(input("Make a guess: "))
        check_answer(guess, answer, turns)

#Track the number of turns and reduce by 1 if they get it wrong.


game()



  