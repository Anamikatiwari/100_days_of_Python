from turtle import Screen, Turtle
from pa

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # control animation


r_paddle = Paddle((350, 0))   # right paddle
l_paddle = Paddle((-350, 0))    # left paddle




def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
    
def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
    

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    
    
    
    
    

screen.exitonclick()