import turtle
import pandas
import numpy as np

screen = turtle.Screen()
screen.title("The U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.addshape(image)
turtle.shape(image)
turtle.penup()
screen.tracer(0)

score = 0
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 states guessed",
                                    prompt="Enter the name of an U.S. State").title()

    if answer_state == "Exit":
        # Creating a missing states and exporting as csv file
        missing_states = np.setdiff1d(state_list, guessed_states)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        x_cor = int(state.x)
        y_cor = int(state.y)
        turtle.setposition(x_cor, y_cor)
        turtle.write(state.state.item())
        score += 1

screen.exitonclick()
