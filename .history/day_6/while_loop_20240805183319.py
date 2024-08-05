""" 
while
---------
while something_is_true
   do something repeatedly
   
"""

#hurdle solution

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
    
for step in range(6):
    jump() 
    

numbers_of_hurdles = 6