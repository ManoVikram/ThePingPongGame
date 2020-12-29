from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

rightPaddle = Paddle((350, 0))
leftPaddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Scoreboard()

#paddle = Turtle()
#paddle.penup()
#paddle.shape("square")
#paddle.color("white")
#paddle.shapesize(stretch_wid=4, stretch_len=1)
#paddle.goto(349, 0)
#
#def go_up():
#    newY = paddle.ycor() + 27
#    paddle.goto(paddle.xcor(), newY)
#
#def go_down():
#    newY = paddle.ycor() - 27
#    paddle.goto(paddle.xcor(), newY)


screen.listen()
screen.onkey(rightPaddle.go_up, "Up")
screen.onkey(rightPaddle.go_down, "Down")

screen.onkey(leftPaddle.go_up, "w")
screen.onkey(leftPaddle.go_down, "s")

gameOn = True
while gameOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if (ball.distance(rightPaddle) < 50 and ball.xcor() > 320) or (ball.distance(leftPaddle) < 50 and ball.xcor() < -320):
        ball.bounceX()

    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.increaseRight()

    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.increaseLeft()
             
screen.exitonclick()

