from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.display_level()

    def over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=FONT )

    def display_level(self):
        self.clear()
        self.goto(-230,250)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.display_level()