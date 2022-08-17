import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25 - CSV and Pandas\States Game\\blank_states_img.gif"
screen.bgpic(image)
data = pandas.read_csv("Day 25 - CSV and Pandas\States Game\\50_states.csv")
states = data.state.to_list()
guessed_states = []

num_correct = 0
while num_correct < 50:
    answer_state = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        j = pandas.DataFrame(missing_states)    
        j.to_csv("missed_states.csv")
        break
    
    if answer_state in states:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        x_cor = int(state.x)
        y_cor = int(state.y)
        num_correct += 1
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(x_cor, y_cor)
        turtle.write(answer_state)



turtle.mainloop()
