from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -280)
        self.left(90)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(0, new_y)