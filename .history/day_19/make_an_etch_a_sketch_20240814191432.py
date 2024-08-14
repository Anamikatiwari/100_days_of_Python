"""  
W = Forwards
S = Backwards
A = Counter-Clockwise
D = Clockwise
C = Clear drawing

"""

from turtle import Turtle, Screen

tim = Turtle()
Screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    

Screen.listen()
Screen.onkey(move_formards, "w")
Screen.onkey(move_backward, "s")
Screen.onkey(turn_left, "a")
Screen.onkey(turn_right, "d")
Screen.exitonclick()

