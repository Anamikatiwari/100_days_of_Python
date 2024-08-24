from turtle import Turtle

class Paddle:
    
    def __init__(self):
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(350, 0)