from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0

    def updateScoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftScore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rightScore, align="center", font=("Courier", 80, "normal"))

    def increaseLeft(self):
        self.leftScore += 1
        self.updateScoreboard()

    def increaseRight(self):
        self.rightScore += 1
        self.updateScoreboard()
