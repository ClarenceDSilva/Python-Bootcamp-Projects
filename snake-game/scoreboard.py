from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.write_score(self.high_score)
        self.score = 0
        self.update_score()

    def write_score(self, high_score):
        with open("high_score.txt", mode="w") as file:
            file.write(str(high_score))

    def read_score(self):
        with open("high_score.txt", mode="r") as file:
            return int(file.read())

    # Replaced by the reset method
    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
