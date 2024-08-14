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
    

creen.listen()
creen.onkey(move_forwards, "w")
creen.onkey(move_backwards, "s")
creen.onkey(turn_left, "a")
creen.onkey(turn_right, "d")
creen.onkey(clear, "c")
creen.exitonclick()
