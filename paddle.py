from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(position)
        
    def go_up(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def go_down(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)
