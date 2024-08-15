from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.pe
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while  game_is_on:
    for segment in segments:
        seg.forward(20)



screen.exitonclick()