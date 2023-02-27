from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        rand_xcor = random.randint(-280, 280)
        rand_ycor = random.randint(-280, 280)
        self.goto(rand_xcor, rand_ycor)