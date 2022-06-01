from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
LEFT = 180
RIGHT = 0

#Snake Class
class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    # Constructor to create initialize the snake
    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.addSegment(position)

    #Method to move
    def move(self):
        # for loop to get segments to move the position of the next segment
        # the range goes from the last segment in the list to the first one
        for segmentNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segmentNum - 1].xcor()
            newY = self.segments[segmentNum - 1].ycor()
            self.segments[segmentNum].goto(newX, newY)

        self.head.forward(MOVE_DISTANCE)
    #method to move up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    #method to move down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    #method to move left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    #method to move right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.addSegment(self.segments[-1].position())

    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]