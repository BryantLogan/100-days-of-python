from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# tom = Turtle(shape="turtle")
# tom.color(colors[1])
# tom.penup()
# tom.goto(x=-230,y=-60)

# joe = Turtle(shape="turtle")
# joe.color(colors[2])
# joe.penup()
# joe.goto(x=-230,y=-20)

# jim = Turtle(shape="turtle")
# jim.color(colors[3])
# jim.penup()
# jim.goto(x=-230,y=20)

# kim = Turtle(shape="turtle")
# kim.color(colors[4])
# kim.penup()
# kim.goto(x=-230,y=60)

# jon = Turtle(shape="turtle")
# jon.color(colors[5])
# jon.penup()
# jon.goto(x=-230,y=100)




screen.exitonclick()