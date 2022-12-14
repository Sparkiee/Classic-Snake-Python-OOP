import turtle
from turtle import Turtle, Screen
import random


class Snake:
    def __init__(self):
        self.timer = 1
        self.draw_score = Turtle()
        self.draw_score.color("white")
        self.draw_score.hideturtle()
        self.draw_score.penup()
        self.draw_score.setpos(0, 275)
        self.draw_score.write(f"Score: 0", font=("Arial", 20), align="center")

        self.score = 0
        self.food = []
        self.food_draw = Turtle()
        self.food_draw.shape("circle")
        self.food_draw.color("blue")
        self.food_draw.penup()
        self.heading = 0
        self.start_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.body = []
        for i in self.start_positions:
            self.body.append(Turtle())
            self.body[len(self.body) - 1].penup()
            self.body[len(self.body) - 1].color("white")
            self.body[len(self.body) - 1].shape("square")
            self.body[len(self.body) - 1].goto(self.start_positions[len(self.body) - 1])
        print(self.body[0].heading())
        # self.screen.update()

    def getLead(self):
        return self.body[0]

    def drop_food(self):
        x = round(random.randint(-300, 300) / 20)
        if x < 0:
            x += 1
        else:
            x -= 1
        y = round(random.randint(-300, 300) / 20)
        if y < 0:
            y += 1
        else:
            y -= 1
        self.food.append((x * 20, y * 20))
        self.food_draw.goto(self.food[0][0], self.food[0][1])

    def play(self):
        pos = ""
        self.start_positions.pop()
        if self.body[0].heading() == 0:
            pos = self.start_positions[0][0] + 20, self.start_positions[0][1]
        if self.body[0].heading() == 90:
            pos = self.start_positions[0][0], self.start_positions[0][1] + 20
        if self.body[0].heading() == 180:
            pos = self.start_positions[0][0] - 20, self.start_positions[0][1]
        if self.body[0].heading() == 270:
            pos = self.start_positions[0][0], self.start_positions[0][1] - 20

        self.start_positions.insert(0, pos)
        self.body[len(self.body) - 1].goto(pos)
        self.body[len(self.body) - 1].setheading(self.body[0].heading())
        self.body.insert(0, self.body.pop())

        if self.getLead().pos() == self.food_draw.pos():
            self.food.pop()
            self.drop_food()
            self.score += 1
            if self.score % 2 == 0:
                if self.timer > 0.5:
                    self.timer -= 0.1
                self.body.append(Turtle())
                self.body[len(self.body) - 1].penup()
                self.body[len(self.body) - 1].color("white")
                self.body[len(self.body) - 1].shape("square")
                self.body[len(self.body) - 1].setpos((-600, -600))
            self.draw_score.clear()
            self.draw_score.write(f"Score: {self.score}", font=("Arial", 20), align="center")

        if self.is_out_of_bounds() or self.self_collision():
            turtle.Turtle()
            turtle.color("white")
            turtle.hideturtle()
            turtle.write(f"GAME OVER!", font=("Arial", 25), align="center")
            return False
        return True

    def is_out_of_bounds(self):
        part = self.start_positions[0]
        if part[0] >= 300 or part[1] >= 300 or part[0] <= -300 or part[1] <= -300:
            return True
        return False

    def self_collision(self):
        count = 0
        for i in self.body:
            for j in self.body:
                if i != j and i.pos() == j.pos():
                    return True
        return False
