"""
rules
--------
. rock wins against scissors
. scissors wins against paper
. paper wins against rock
"""
import random

rock = '''
    ________
---'   _____)
      (______)
      (_____)
      (____) 
---.__(___)
      

'''

paper = '''
    ________
---'   _____)____
           ______)
           ________)
          ________)
---.__  _______)  


'''

scissor = '''
    ________
---'    ____)____
           ______)
           ________)
           (___)
---.___    (__)
           
'''

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor")
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")


if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
elif user_choice >= 3 or user_choice <:
    print("You typed an invalid number, you lose!")