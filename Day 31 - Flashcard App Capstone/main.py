from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#--------------------------- APP FUNCTIONALITY ------------------------------#
try:
    data = pandas.read_csv("Day 31 - Flashcard App Capstone\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Day 31 - Flashcard App Capstone\data\\french_words.csv")
    vocab = original_data.to_dict(orient="records")
else:
    vocab = data.to_dict(orient="records")



def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(vocab)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(vocab_label, text=current_card["French"], fill="black")
    canvas.itemconfig(card_display, image=card_front_img)
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(language_label, text = "English", fill="white")
    canvas.itemconfig(card_display, image=card_back_img)
    canvas.itemconfig(vocab_label, text=current_card["English"], fill="white")

def is_correct():
    global current_card
    vocab.remove(current_card)
    data = pandas.DataFrame(vocab)
    data.to_csv("Day 31 - Flashcard App Capstone\data\words_to_learn.csv", index=False)
    new_word()


#--------------------------- UI SETUP ---------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

# Flashcard canvas
canvas = Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="Day 31 - Flashcard App Capstone\images\card_front.png")
card_back_img = PhotoImage(file="Day 31 - Flashcard App Capstone\images\card_back.png")
card_display = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2, sticky="EW")

# Correct and Wrong Buttons
correct_img = PhotoImage(file="Day 31 - Flashcard App Capstone\images\\right.png")
correct_button = Button(image= correct_img, highlightthickness=0,command=is_correct)
correct_button.grid(column=1, row=2)

wrong_img = PhotoImage(file="Day 31 - Flashcard App Capstone\images\wrong.png")
wrong_button = Button(image= wrong_img, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=2)

# Language canvas
language_label = canvas.create_text(400, 150, text= "French", font= ("arial", 40, "italic"))
vocab_label = canvas.create_text(400, 263, text= "Vocab", font= ("arial", 60, "bold"))

# Flipping the flashcard
new_word()


window.mainloop()