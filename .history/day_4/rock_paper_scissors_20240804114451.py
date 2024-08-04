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
game_images = [rock, paper, scissor]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n")
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
