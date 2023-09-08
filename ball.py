from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_now = 0.05
        self.speed("slow")
        self.penup()
        self.shape("circle")
        self.color("yellow")

        self.x_direction = 10
        self.y_direction = 10

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1

    def reset(self):
        self.home()
        self.bounce_x()
        self.speed_now = 0.05

    def speed_up(self):
        self.speed_now *= 0.9
