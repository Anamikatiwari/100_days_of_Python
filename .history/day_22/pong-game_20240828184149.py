from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

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
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor < -280:
        ball.bounce()
    
    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        
    
    
screen.exitonclick()



