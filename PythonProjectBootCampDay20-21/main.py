from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")



while snake.game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.current_score()

    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        snake.game = False
        score.game_over()

    for tail in snake.new_segment[1::]:
        if snake.head.distance(tail) < 20:
            snake.game = False
            score.game_over()

screen.exitonclick()