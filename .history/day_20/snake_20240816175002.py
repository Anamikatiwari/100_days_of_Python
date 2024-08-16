from turtle import Screen
from snake import Snake 
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()

