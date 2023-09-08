from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)

        self.l_score = 0
        self.r_score = 0

    def update(self):
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", False, ALIGN, FONT)
