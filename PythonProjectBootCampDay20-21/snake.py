from turtle import Turtle

SEGMENT = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:

    def __init__(self):
        self.new_segment = []
        self.creat_snake()
        self.head = self.new_segment[0]
        self.game = True

    def creat_snake(self):
        for position in SEGMENT:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.speed("fastest")
        snake.penup()
        snake.goto(position)
        self.new_segment.append(snake)

    def extend(self):
        self.add_snake(self.new_segment[-1].position())

    def move(self):
        for seg_num in range(len(self.new_segment) - 1, 0, -1):
            x = self.new_segment[seg_num - 1].xcor()
            y = self.new_segment[seg_num - 1].ycor()
            self.new_segment[seg_num].goto(x, y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)