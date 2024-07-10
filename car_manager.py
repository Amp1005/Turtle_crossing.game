from turtle import Turtle
from random import *
from player import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# player = Player()
class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        y = randint(1,5)
        if y==1:
            new_car = Turtle('square')
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-230,230)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):

        for car in self.all_cars:
            car.backward(self.car_speed)

    def move_increment(self):
        self.car_speed += MOVE_INCREMENT










