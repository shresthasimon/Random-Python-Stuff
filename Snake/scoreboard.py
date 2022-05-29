from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.updateScoreBoard()

    #constructor to create writing
    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))

    #method to increase score by 1
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER LOSER", align="center", font=("Courier", 18, "normal"))