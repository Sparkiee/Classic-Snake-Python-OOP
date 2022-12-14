from turtle import Screen, Turtle
from Snake import Snake
import time
import random

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.update()
screen.bgcolor("black")
screen.title("The Best Snake Game in Existence")
screen.listen()


def update_up():

    if s.getLead().heading() == 0.0 or s.getLead().heading() == 180.0:
        s.getLead().setheading(90)


def update_down():
    if s.getLead().heading() == 0.0 or s.getLead().heading() == 180.0:
        s.getLead().setheading(270)


def update_right():
    if s.getLead().heading() == 90.0 or s.getLead().heading() == 270.0:
        s.getLead().setheading(0)


def update_left():
    if s.getLead().heading() == 90.0 or s.getLead().heading() == 270.0:
        s.getLead().setheading(180)


s = Snake()
s.drop_food()
game_on = True
while game_on:
    game_on = s.play()
    screen.update()
    screen.onkeypress(fun=update_up, key="w")
    screen.onkeypress(fun=update_down, key="s")
    screen.onkeypress(fun=update_left, key="a")
    screen.onkeypress(fun=update_right, key="d")
    time.sleep(s.timer)

screen.exitonclick()
