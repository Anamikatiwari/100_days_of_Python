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

if computer_choice > user