# from turtle import Screen
# from snake import Snake 
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake game")
# screen.tracer(0)

# snake = Snake()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
    
#     snake.move()
    
    
    
    
# screen.exitonclick()
from turtle import T

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)