from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 260)
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score : {self.count} High Score : {self.high_score}", False, align=ALIGN, font=FONT)
        self.update_score()

    def current_score(self):
        self.count += 1
        self.update_score()

    def reset_score(self):
        if self.count > self.high_score:
            with open("data.txt", "w") as file:
                self.high_score = self.count
                file.write(f"{self.high_score}")
        self.count = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.count} High Score : {self.high_score}", False, align=ALIGN, font=FONT)