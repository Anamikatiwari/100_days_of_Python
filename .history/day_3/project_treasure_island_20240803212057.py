print("Welcom to Trasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "Wait":
       choice3 = input ("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which color do you choose?").lower()
       if choice3 == "red":
           print("")
       elif choice3 == "yellow":
       elif choice3 == "blue":
       else:
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole, Game Over.")

 
