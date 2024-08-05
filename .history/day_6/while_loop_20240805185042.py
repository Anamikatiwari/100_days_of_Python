""" 
while Loop
---------
while something_is_true
   #do this
   #then do this
   #then do this
   
"""
# Reeborg's World
#hurdle solution using while loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    


numbers_of_hurdles = 6
while numbers_of_hurdles > 0:
    jump()
    numbers_of_hurdles -= 1
    print(numbers_of_hurdles)
    

#hurdle 2 solution using while loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    
    # for step in range(6):
    #     jump()

while not at_goal(): 
    jump()

#hurdle 3 