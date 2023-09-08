from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(x, y)

        self.move_increment = 20

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + self.move_increment)
            if self.move_increment < 100:
                self.move_increment += 5

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - self.move_increment)
            if self.move_increment < 100:
                self.move_increment += 5

    def reset_speed(self):
        self.move_increment = 20
