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

def move_formards():
    tim.forward(10)

Screen.listen()
Screen.onkey(move_formards, "w")
Screen.onkey(move_backward, "s")
Screen.onkey(turn_left, "a")
Screen.onkey(turn_right, "d")
Screen.exitonclick()