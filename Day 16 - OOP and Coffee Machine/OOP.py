# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(150)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# import another_module
# print(another_module.another_variable)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"]) 
table.add_column("Type", ["Electric","Water","Fire"]) 
table.align = "r"
print(table)
