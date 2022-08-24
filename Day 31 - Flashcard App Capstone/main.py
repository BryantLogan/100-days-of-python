from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

# Flashcard canvas
canvas = Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="Day 31 - Flashcard App Capstone\images\card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2, sticky="EW")

# Correct and Wrong Buttons
correct_img = PhotoImage(file="Day 31 - Flashcard App Capstone\images\\right.png")
correct_button = Button(image= correct_img, highlightthickness=0)
correct_button.grid(column=1, row=2)

wrong_img = PhotoImage(file="Day 31 - Flashcard App Capstone\images\wrong.png")
wrong_button = Button(image= wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=2)

# Language canvas
language_label = canvas.create_text(400, 150, text= "English", font= ("arial", 40, "italic"))
vocab_label = canvas.create_text(400, 263, text= "Vocab", font= ("arial", 60, "bold"))


window.mainloop()