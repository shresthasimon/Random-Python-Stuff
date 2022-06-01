from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

#setting up the screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


#initializing snake, food, and scoreboard
snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

#setting up listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameIsPlaying = True
while gameIsPlaying:
    screen.update()
    time.sleep(.1)
    snake.move()

    #detection for snake eating food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increaseScore()

    #Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.reset()
            snake.reset()





screen.exitonclick()