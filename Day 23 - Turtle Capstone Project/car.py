from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        all_cars = []

        super().__init__()

    
    def create_cars(self):
        self.shape("square")
        self.color(COLORS[random.randint(0,5)])
        self.shapesize(stretch_wid=0.75, stretch_len=2)
        self.penup()
        y_start = random.randint(-280, 280)
        self.goto(250, y_start)

    def move(self):
        speed = STARTING_MOVE_DISTANCE
        new_x = self.xcor() - speed
        new_y = self.ycor()
        self.goto(new_x, new_y)


