from turtle import Screen, Turtle
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




# snake2 = Turtle()
# snake2.shape("square")
# snake2.color("white")
# snake2.goto(x=-20, y=0)

# snake3 = Turtle()
# snake3.shape("square")
# snake3.color("white")
# snake3.goto(x=-40, y=0)





screen.exitonclick()