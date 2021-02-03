from turtle import Turtle

FONT = ("Arial", 10, "normal")


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_state_name(self, state_name, state_x_cor, state_y_cor):
        self.setposition(state_x_cor, state_y_cor)
        self.write(state_name, align="center", font=FONT)
