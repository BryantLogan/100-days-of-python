import random

player_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0,2)

if player_choice >= 3 or player_choice < 0:
    print("You chose an invalid number. You lose!")
elif player_choice == 0:
    if computer_choice == 1:
        print("You chose Rock\nComputer chose paper. Game Over!")
    elif computer_choice == 0:
        print("It's a tie! You both chose rock")
    else:
        print("You chose rock\nComputer chose scissors. You win!")
elif player_choice == 1:
    if computer_choice == 0:
        print("You chose Paper\nComputer chose rock. You win!")
    elif computer_choice == 1:
        print("It's a tie! You both chose paper")
    else:
        print("You chose paper\nComputer chose scissors. You lose!")
elif player_choice == 2:
    if computer_choice == 1:
        print("You chose scissors\nComputer chose paper. You win!")
    elif computer_choice == 0:
        print("You chose scissors\nComputer chose rock. You lose!")
    else:
        print("You chose scissors\nComputer chose scissors. It's a tie")