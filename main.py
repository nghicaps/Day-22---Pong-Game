import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeyrelease(r_paddle.reset_speed, "Up")
screen.onkeyrelease(r_paddle.reset_speed, "Down")
screen.onkeyrelease(l_paddle.reset_speed, "w")
screen.onkeyrelease(l_paddle.reset_speed, "s")

game = True
while game:
    screen.update()
    time.sleep(ball.speed_now)
    ball.move()
    scoreboard.update()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) <= 60 and ball.xcor() == 330) or (
        ball.distance(l_paddle) <= 60 and ball.xcor() == -330
    ):
        ball.bounce_x()
        ball.speed_up()

    if ball.xcor() > 420:
        scoreboard.l_score += 1
        ball.reset()
    elif ball.xcor() < -420:
        scoreboard.r_score += 1
        ball.reset()

screen.exitonclick()
