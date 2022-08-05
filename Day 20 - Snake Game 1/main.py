from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

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





# snake2 = Turtle()
# snake2.shape("square")
# snake2.color("white")
# snake2.goto(x=-20, y=0)

# snake3 = Turtle()
# snake3.shape("square")
# snake3.color("white")
# snake3.goto(x=-40, y=0)





screen.exitonclick()