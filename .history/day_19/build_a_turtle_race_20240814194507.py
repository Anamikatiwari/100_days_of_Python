from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(0, 6):
    = Turtle(shape="turtle")
   .color(colors[turtle_index])
   .penup()
   .goto(x=-230, y=y_position[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)

screen.exitonclick()