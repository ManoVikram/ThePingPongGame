from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        newX = self.xcor() + 10
        newY = self.ycor() + 10
        self.goto(newX, newY)
