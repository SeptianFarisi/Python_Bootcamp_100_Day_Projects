from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_score()


    def level_up(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-290, 250)
        self.write(f"Level : {self.level}", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)