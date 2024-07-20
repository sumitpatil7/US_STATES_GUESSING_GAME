import turtle
import pandas

from turtle import Screen, Turtle

image = "blank_states_img.gif"
timmy = Turtle()
screen = Screen()
screen.title("U.S. States' Guessing Game")
screen.addshape(image)
turtle.shape(image)
guessed_states = []
is_game_on = True
i = 0
data = pandas.read_csv("50_states.csv")
while len(guessed_states) < 50:

    answer_state = screen.textinput(f"{i} of 50 guessed", "What is the state that you know? ").title()
    if answer_state == "Exit":
        print("States You did not guess: ")
        print(list(data["state"]))
        data["state"].to_csv("Missing")
        break

    state_list = data.state.to_list()
    for state in state_list:
        if answer_state == state:
            i += 1
            guessed_states.append(state)
            current_state = data[(data.state == state)]
            x_cor = int(current_state["x"].values[0])
            y_cor = int(current_state["y"].values[0])
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(x_cor, y_cor)
            timmy.write(state)
            data = data[data.state != answer_state]


