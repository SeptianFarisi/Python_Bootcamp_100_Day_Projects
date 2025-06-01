from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.speed_up = 0.1
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.speed_up *= 0.9