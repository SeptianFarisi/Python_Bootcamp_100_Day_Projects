import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Capstone")
screen.listen()

score = Scoreboard()
player = Player()
screen.onkey(player.move, "Up")
all_car = []
for _ in range(6):
    car = CarManager()
    all_car.append(car)

game_is_on = True
while game_is_on:
    time.sleep(player.speed_up)
    screen.update()

    # Detect Y coordinate
    if player.ycor() > 280:
        player.finish()
        score.level_up()

    # Create cars and move it
    for cars in all_car:
        cars.move()

        # Detect X coordinate to add cars
        if cars.xcor() < -300:
            cars.add_car()

        # Detect collision player and cars
        if player.distance(cars) < 30:
            score.game_over()
            game_is_on = False

screen.exitonclick()