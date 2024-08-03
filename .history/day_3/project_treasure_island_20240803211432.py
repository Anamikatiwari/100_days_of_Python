print("Welcom to Trasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "swim" to swim across.').lower()
else:
    print("You fell into a hole, Game Over.")

 
