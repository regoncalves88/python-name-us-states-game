from turtle import Turtle

TOTAL_STATES = 50


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.total_states = TOTAL_STATES
        self.total_score = 0

    def increase_score(self):
        self.total_score += 1
