from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        random_x = random.randint(-300, 300)
        random_y = random.randint(-150, 150)
        self.goto(random_x, random_y)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def add_car(self):
        self.color(random.choice(COLORS))
        random_y = random.randint(-150, 150)
        self.goto(300, random_y)