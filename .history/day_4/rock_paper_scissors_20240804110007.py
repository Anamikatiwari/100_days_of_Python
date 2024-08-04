"""
rules
--------
. rock wins against scissors
. scissors wins against paper
. paper wins against rock
"""
import random

rock = '''
✊ ______
---'   ___)
      (____)
      (___)
      (___)
'''

paper = '''
🫱
'''

scissor = '''
✌️
'''

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor")