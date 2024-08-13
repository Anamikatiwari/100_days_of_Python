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
import random

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)
        
for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
    
    
   # 4. draw a Random Walk
import turtle as t
import random

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 100, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    
    
    
    
    # 5. make a Spirograph
     
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
    
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
    


    
    
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


# Random color   :   using RGB

 
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
    

directions = [0, 90, 100, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
    

