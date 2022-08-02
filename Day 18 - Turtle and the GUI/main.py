from turtle import Turtle
from turtle import Screen
import random

timmy_the_turtle = Turtle()
# # timmy_the_turtle.shape("turtle")
# # timmy_the_turtle.color("red")
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Draws a square
def draw_shape(sides):
    angle = 360 / sides
    for moves in range(sides):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(angle)


for shape_side_n in range (3,11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

# #aliasing 
# import turtle as t
# tim = t.Turtle() # good for modules with long names



screen = Screen()
screen.exitonclick()