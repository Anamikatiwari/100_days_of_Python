# import another_module
# print(another_module.another_variable)


# import turtle
from turtle import Turtle, Screen
# constructing object 
# timmy = turtle.Turtle()
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

'''   
objects
  |
  |
  car.speed
        |
        |
        attribute
'''
my_screen = Screen()
print(my_screen.canvheight)
# object method
my_screen.exitonclick()

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Python packages
   # pypi(python package index) :   prettyTable-pypi
   # 

from prettytable import PrettyTable
table = PrettyTable     # pascal-case
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric"])

print(table)