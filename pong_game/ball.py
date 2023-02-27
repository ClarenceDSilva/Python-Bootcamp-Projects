import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0, 0)
        self.x_pos = 10
        self.y_pos = 10

    def move(self):
        x_cor = self.xcor() + self.x_pos
        y_cor = self.ycor() + self.y_pos
        self.setposition(x_cor, y_cor)

    def change_y_direction(self):
        self.y_pos *= -1

    def change_x_direction(self):
        self.x_pos *= -1

    def reset_position(self):
        self.x_pos = 10
        self.setposition(0, 0)
        self.change_x_direction()
