from turtle import Screen, shape

background = "blank_states_img.gif"

screen = Screen()
screen.title("Name US States Game")
screen.addshape(background)
shape(background)

answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")

screen.exitonclick()
