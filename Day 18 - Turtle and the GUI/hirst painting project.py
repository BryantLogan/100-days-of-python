# from colorgram import *
import turtle as t
from turtle import Screen, color
import random
screen = Screen()

color_list =    [(1, 12, 31), (53, 25, 17), (218, 127, 106),(10, 104, 159), (242, 213, 68), (149, 83, 39),
                (215, 87, 63),(155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104),
                (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207),
                (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216),
                (100, 218, 229), (117, 171, 192), (79, 135, 178)
              ]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

def draw_hirst():
    for dot_count in range(1, number_of_dots +1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

draw_hirst()



screen.exitonclick()