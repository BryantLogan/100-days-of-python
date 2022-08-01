import random

easy_level_turns = 10
hard_level_turns = 5

def check_answer(user_guess,secret_number, turns):
    """checks answer against guess, returns the number of turns remaining"""
    if user_guess > secret_number:
        print("Too high.")
        return turns - 1
    if user_guess < secret_number:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {secret_number}.")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    if difficulty == "easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1,100)

    turns = set_difficulty()

    user_guess = 0
    while user_guess != secret_number:
        print(f"You have {turns} attempt(s) remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, secret_number, turns)
        if turns == 0:
            print("You've run out of guesses, You lose.")
            return
        elif user_guess != secret_number:
            print("Guess again.")

game()

##### MY OWN CODE #####

# game_over = False
# if difficulty == "easy":
#     lives = 10
#     while game_over is False:
#         while lives > 0:
#             user_guess = int(input("Make a guess: "))
#             if user_guess > secret_number:
#                 lives -= 1
#                 if lives == 0:
#                     print("Too high.\nYou ran out of guesses. You lose.")
#                     game_over = True
#                     exit()
#                 print("Too high.\nGuess again.")
#                 print(f"You have {lives} attempt(s) remaining to guess the number.")
#             elif user_guess < secret_number:
#                 lives -= 1
#                 if lives == 0:
#                     print("Too low.\nYou ran out of guesses. You lose.")
#                     game_over = True
#                     exit()
#                 print("Too low.\nGuess again.")
#                 print(f"You have {lives} attempt(s) remaining to guess the number.")
#             else:
#                 print(f"You got it! The answer was {secret_number}.")
#                 game_over = True
#                 exit()
# if difficulty == "hard":
#     lives = 5
#     while game_over is False:
#         while lives > 0:
#             user_guess = int(input("Make a guess: "))
#             if user_guess > secret_number:
#                 lives -= 1
#                 if lives == 0:
#                     print("Too high.\nYou ran out of guesses. You lose.")
#                     game_over = True
#                     exit()
#                 print("Too high.\nGuess again.")
#                 print(f"You have {lives} attempt(s) remaining to guess the number.")
#             elif user_guess < secret_number:
#                 lives -= 1
#                 if lives == 0:
#                     print("Too low.\nYou ran out of guesses. You lose.")
#                     game_over = True
#                     exit()
#                 print("Too low.\nGuess again.")
#                 print(f"You have {lives} attempt(s) remaining to guess the number.")
#             else:
#                 print(f"You got it! The answer was {secret_number}.")
#                 game_over = True
#                 exit()