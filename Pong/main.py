from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

#Screen initialization
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

#Initialize class objects
ball = Ball()
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
scoreboard = ScoreBoard()

#Listen for key strokes for game
screen.listen()
screen.onkey(paddle1.goUp, "Up")
screen.onkey(paddle1.goDown, "Down")
screen.onkey(paddle2.goUp, "w")
screen.onkey(paddle2.goDown, "s")


gameIsPlaying = True
while gameIsPlaying:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    #detection for ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    #detection for ball collision with paddle
    if (ball.distance(paddle2) < 50 and ball.xcor() > -340) or (ball.distance(paddle1) < 50 and ball.xcor() < 340):
        ball.bounceX()

    #Detection when paddle misses ball
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.lPoint()

    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.rPoint()


screen.exitonclick()