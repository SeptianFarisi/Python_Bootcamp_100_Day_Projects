from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

screen.listen()
game = True

computer = Paddle((350,0))
player = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")
screen.onkey(computer.go_up, "Up")
screen.onkey(computer.go_down, "Down")

while game:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(computer) < 50 and ball.xcor() < 330 or ball.distance(player) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        hit = 0
        score.r_point()
    if ball.xcor() < -380:
        ball.reset()
        hit = 0
        score.l_point()

screen.exitonclick()