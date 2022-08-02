import random
from hangmanwords import hanglist
from hangman_art import logo, stages

lives = 6
chosen_word = random.choice(hanglist)
print(logo)
# print(f"Psst, the solution is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}")
joined_word = "".join(display)


while joined_word != chosen_word:
    guess = input("Guess a letter: ").lower()
    if lives > 0:
        if guess in display:
            print(f"You've already guessed {guess}")
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                joined_word = "".join(display)
                print(stages[lives]) 
        print(f"{' '.join(display)}")  
        if guess not in chosen_word:
            print(f"You guessed {guess}. That's not in the word. You lose a life.")
            lives -=1
            print(stages[lives])
    if lives == 0:
        print(f"You lose. The word was {chosen_word}.")
        exit()
print("Congratulations! You win!")