from turtle import Screen, Turtle
from Snake import Snake
from Food import Food
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

    if s.getHead().heading() == 0.0 or s.getHead().heading() == 180.0:
        s.getHead().setheading(90)


def update_down():
    if s.getHead().heading() == 0.0 or s.getHead().heading() == 180.0:
        s.getHead().setheading(270)


def update_right():
    if s.getHead().heading() == 90.0 or s.getHead().heading() == 270.0:
        s.getHead().setheading(0)


def update_left():
    if s.getHead().heading() == 90.0 or s.getHead().heading() == 270.0:
        s.getHead().setheading(180)


s = Snake()
food = Food()

screen.onkeypress(fun=update_up, key="w")
screen.onkeypress(fun=update_down, key="s")
screen.onkeypress(fun=update_left, key="a")
screen.onkeypress(fun=update_right, key="d")

game_on = True
while game_on:
    screen.update()
    game_on = s.play()
    # eating food
    if s.getHead().distance(food) < 15:
        s.score += 1
        s.update_score()
        food.move()
        # tuning up the game tension!
        if s.score % 2 == 0:
            s.increase_snake()
            s.increase_speed()
    time.sleep(s.timer)

screen.exitonclick()
