from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(-100, 230)
        self.write(self.left_score, align="center", font=('Courier', 50, 'normal'))
        self.setposition(100, 230)
        self.write(self.right_score, align="center", font=('Courier', 50, 'normal'))

    def increase_l_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.right_score += 1
        self.update_scoreboard()
