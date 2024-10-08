from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # control animation


r_paddle = Paddle((350, 0))   # right paddle
l_paddle = Paddle((-350, 0))    # left paddle
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    
    
    
    
    

screen.exitonclick()