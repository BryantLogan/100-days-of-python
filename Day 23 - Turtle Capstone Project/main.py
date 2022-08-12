import time
from turtle import Screen
from player import Player
from car import CarManager
#from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player((0,-280))
car = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.move()
    screen.update()








screen.exitonclick()