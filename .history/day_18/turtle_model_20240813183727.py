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
    
    

  # 2. Draw a Dashed line
import turtle as t 

tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    
    
    
    # 3. Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
import turtle as t

tim = t.Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)
        
for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    
    
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


### Aliasing Modules
import turtle as t

tim = t.Turtle()



### Installing Modules
  # pip install heroes
 #usage
import heroes      
print(heroes.gen())

#---------------------------------------------------------------------------



