from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, tupple):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(tupple)

    def move(self):
        while True:
            if self.goto(self.xcor(), self.ycor() > 300):
                self.go_down()
            elif self.goto(self.xcor(), self.ycor() < -300):
                self.go_up()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)