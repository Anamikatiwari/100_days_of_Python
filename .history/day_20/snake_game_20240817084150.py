from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeysnake.up, "Up")
screen.onkey("Down")
screen.onkey("Left")
screen.onkey("Right")

game_is_on = True
while  game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

        
screen.exitonclick()

