from turtle import Screen, shape
from writer import Writer
from score import Score
import pandas as pd

background = "blank_states_img.gif"
states = pd.read_csv("50_states.csv")
guessed_states = []
missing_states = []

screen = Screen()
screen.title("Name US States Game")
screen.addshape(background)
shape(background)

score = Score()
writer = Writer()

while score.total_score < 50:
    answer = screen.textinput(title=f"{score.total_score} / {score.total_states} States Correct", prompt="What's"
                              " another state's name?").title()
    if answer == "Exit":
        for state in states["state"]:
            if state not in guessed_states:
                missing_states.append(state)

        missing_states_data = pd.DataFrame(missing_states)
        missing_states_data.to_csv("states_to_be_learned.csv")
        break
    else:
        for state in states["state"]:
            if answer == state:
                state_xcor = int(states["x"][states["state"] == answer])
                state_ycor = int(states["y"][states["state"] == answer])
                writer.write_state_name(answer, state_xcor, state_ycor)
                score.increase_score()
                guessed_states.append(answer)
