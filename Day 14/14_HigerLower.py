from gamedata import data
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

print(logo)


def game():
    random_a = random.choice(data)
    random_b = random.choice(data)
    follower_count_a = random_a['follower_count']
    follower_count_b = random_b['follower_count']
    score = 0
    
    print(f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}.\n")
    print(vs)
    print(f"Against: {random_b['name']}, a {random_b['description']}, from {random_b['country']}.")
    
    higher_lower = True
    while higher_lower is True:
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess == "A" and follower_count_a > follower_count_b:
            random_b = random.choice(data)
            follower_count_b = random_b['follower_count']
            score += 1
            print(f"You're right! Current score: {score}")
            print(f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}.\n")
            print(vs)
            print(f"Against: {random_b['name']}, a {random_b['description']}, from {random_b['country']}.")
            higher_lower = True
        elif guess == "B" and follower_count_b > follower_count_a:
            random_a = random_b
            follower_count_a = random_b['follower_count']
            random_b = random.choice(data)
            follower_count_b = random_b['follower_count']
            score += 1
            print(f"You're right! Current score: {score}")
            print(f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}.\n")
            print(vs)
            print(f"Against: {random_b['name']}, a {random_b['description']}, from {random_b['country']}.")
            higher_lower = True
        elif guess == "A" and follower_count_a < follower_count_b:
            print(f"Sorry, that's wrong. Final score: {score}")
            higher_lower = False
        elif guess == "B" and follower_count_b < follower_count_a:
            print(f"Sorry, that's wrong. Final score: {score}")
            higher_lower = False

game()