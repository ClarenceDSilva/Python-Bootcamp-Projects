from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
score = Score()

# Start listening to keystrokes
screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detecting collisions on top and bottom walls
    if ball.ycor() not in range(-285, 286):
        ball.change_y_direction()

    # Detecting collisions with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_pos *= 2
        ball.change_x_direction()

    # Detecting collision with the right wall
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l_score()

    # Detecting collision with the left wall
    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r_score()

screen.exitonclick()
