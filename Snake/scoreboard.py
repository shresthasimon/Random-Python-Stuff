from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as data:
            self.highScore = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.updateScoreBoard()


    #constructor to create writing
    def updateScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", align="center", font=("Courier", 18, "normal"))

    #method to increase score by 1
    def increaseScore(self):
        self.score += 1
        self.updateScoreBoard()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highscore.txt","w") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.updateScoreBoard()

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER LOSER", align="center", font=("Courier", 18, "normal"))