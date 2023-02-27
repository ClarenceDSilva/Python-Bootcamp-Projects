from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def paddle_up(self):
        self.goto(self.xcor(), self.ycor() + 50)

    def paddle_down(self):
        self.goto(self.xcor(), self.ycor() - 50)
