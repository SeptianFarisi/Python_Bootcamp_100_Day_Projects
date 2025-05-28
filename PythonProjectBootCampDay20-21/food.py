from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1.0, stretch_len=1.0)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.goto(x, y)