from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick(),

#------------------------------------------

# Turtle challenge
  # 1. Draw a square

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


#-----------------------------------------------------------------

# importing modules 

### basic import
import turtle

tim = turtle.Turtle()


### from ... import ...
from turtle import Turtle

tim = Turtle()
tom = Turtle()


### from turtle import *     : import everything
from turtle import *


# Aliasing Modules
import turtle as t

tim = t.Turtle()



# Installing Modules
import heroes  # pip insta



