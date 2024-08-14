from turtle import Turtle, Screen

tim = Turtle()
Screen = Screen()

def move_formards():
    tim.forward(10)

Screen.listen()
Screen.onkey(key="space", fun=move_formards)
Screen.exitonclick()

# higher order function   :   functions that can accept other functions as arguments, return functions, or both.
