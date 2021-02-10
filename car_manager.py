from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y_COR = [-260, -230, -200, -170, -140, -110, -80, -50, -20, 10, 40, 70, 100, 130, 160, 190, 220, 250]


class CarManager():
    def __init__(self):
        self.all_cars = []

    def new_car(self):
        chance = random.randint(1,6)
        if chance == 2:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.choice(STARTING_Y_COR))
            self.all_cars.append(new_car)


    def move(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)