import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_total = 0
computer_total = 0

def deal_card():
    user_cards.append(cards[random.randint(0,12)])
    while sum(computer_cards) < 17:
        computer_cards.append(cards[random.randint(0,12)])
    else:
        return

def deal_computer():
    while sum(computer_cards) < 17:
        computer_cards.append(cards[random.randint(0,12)])
    else:
        return

def calculate_score(a):
    return sum(a)

gameover = False
while gameover == False:
    play = "y"
    while play != "n":
        play = input("Do you want to play a game of blackjack? Type 'y' or n': ")
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
        computer_cards = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
        user_total = sum(user_cards)
        computer_total = sum(computer_cards)
        if computer_total == 21:
            print(f"You lose! Computer has blackjack: {computer_cards}")
            gameover = True
        elif user_total == 21:
            print(f"You win! You have blackjack: {user_cards}")
            gameover = True
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)} \nComputer's first card: {computer_cards[0]}")
        while sum(user_cards) <= 21:
            hit = input("Would you like another card? Type 'y' or 'n': ")
            if hit == "y":
                deal_card()
                calculate_score(user_cards)
                calculate_score(computer_cards)
                if sum(user_cards) <= 21:
                    print(f"Your hand: {user_cards}, current score: {calculate_score(user_cards)}\nComputer's first card: {computer_cards[0]}")
                elif sum(user_cards) > 21:
                    print(f"You went over!\nYour final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, Computer final score: {calculate_score(computer_cards)}\nYou Lose!")
            elif hit == "n":
                deal_computer()
                calculate_score(user_cards)
                calculate_score(computer_cards)
                if sum(user_cards) > sum(computer_cards) and sum(user_cards) <= 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, Computer final score: {calculate_score(computer_cards)}\nYou Win!")
                elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) <= 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, Computer final score: {calculate_score(computer_cards)}\nYou Lose!")
                elif sum(computer_cards) == 21 and sum(computer_cards) == 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, Computer final score: {calculate_score(computer_cards)}\nIt's a Tie!")    
                elif sum(computer_cards) == sum(user_cards) and sum(computer_cards) <= 21 and sum(user_cards) <= 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, Computer final score: {calculate_score(computer_cards)}\nIt's a Tie!")
                elif sum(user_cards) < 21 and sum(computer_cards) > 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, Computer final score: {calculate_score(computer_cards)}\nYou Win!")
                elif sum(computer_cards) < 21 and sum(user_cards) > 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, Computer final score: {calculate_score(computer_cards)}\nYou Win!")
                elif sum(user_cards) == 21 and sum(computer_cards) > 21 or sum(computer_cards) < 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}\nComputer's final hand: {computer_cards}, Computer final score: {calculate_score(computer_cards)}\nYou Win!")
                play_again = input("Do you want to play a game of blackjack? Type 'y' or n': ")
                if play_again == "y":
                    gameover = False
                    play == "y"
                    user_cards = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
                    computer_cards = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
                    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)} \nComputer's first card: {computer_cards[0]}")
                if play_again == "n":
                    print("Thanks for playing. Goodbye!")
                    gameover = True
                    exit()
            else:
                print("Invalid Entry")



# print(f"Your current hand: {user_cards}, current score: {calculate_score(user_cards)}\nComputer's hand: {computer_cards}, final score: {calculate_score(computer_cards)}")


#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
