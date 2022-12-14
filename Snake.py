import turtle
from turtle import Turtle


class Snake:
    def __init__(self):
        self.timer = 0.5
        self.draw_score = Turtle()
        self.draw_score.color("white")
        self.draw_score.hideturtle()
        self.draw_score.penup()
        self.draw_score.setpos(0, 275)
        self.draw_score.write(f"Score: 0", font=("Arial", 20), align="center")

        self.score = 0

        self.heading = 0
        self.start_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.body = []
        for i in self.start_positions:
            self.body.append(Turtle())
            self.body[len(self.body) - 1].penup()
            self.body[len(self.body) - 1].color("white")
            self.body[len(self.body) - 1].shape("square")
            self.body[len(self.body) - 1].goto(self.start_positions[len(self.body) - 1])

    def getHead(self):
        return self.body[0]

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
        for i in self.body[1:]:
                if i.pos() == self.getHead().pos():
                    return True
        return False

    def increase_snake(self):
        self.body.append(Turtle())
        self.body[len(self.body) - 1].penup()
        self.body[len(self.body) - 1].color("white")
        self.body[len(self.body) - 1].shape("square")
        self.body[len(self.body) - 1].setpos((-600, -600))

    def increase_speed(self):
        if self.timer >= 0.2:
            self.timer -= 0.1

    def update_score(self):
        self.draw_score.clear()
        self.draw_score.write(f"Score: {self.score}", font=("Arial", 20), align="center")