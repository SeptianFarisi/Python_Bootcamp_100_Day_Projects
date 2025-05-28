from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score : {self.count}", False, align=ALIGN, font=FONT)
        self.update_score()

    def current_score(self):
        self.count += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGN, font=FONT)

    def update_score(self):
        self.write(f"Score : {self.count}", False, align=ALIGN, font=FONT)