#Reeborg's World
#
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
    jump()  # repeat the jump function 6 times

    
    


