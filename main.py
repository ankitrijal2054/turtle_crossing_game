import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.move()

    # detect collision
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            score.over()
            game_is_on = False

    # detect when layer reach top
    if player.ycor() > 280:
        player.reset_player()
        score.increase_level()
        car.increase_speed()

screen.exitonclick()