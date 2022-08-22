from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    rand_letters = [choice(letters) for num in range(randint(8, 10))]
    rand_numbers = [choice(numbers) for num in range(randint(2, 4))]
    rand_symbols = [choice(symbols) for num in range(randint(2, 4))]
    
    rand_password_list = rand_letters + rand_numbers + rand_symbols
    shuffle(rand_password_list)

    final_password = "".join(rand_password_list)
    password_entry.insert(0, f"{final_password}")
    pyperclip.copy(final_password)
    messagebox.showinfo(title="Password copied", message="Your password has been copied to your clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_creds():
    website = website_entry.get()
    user_name = userinfo_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {user_name}\nPassword: {password}\nIs it OK to save?")

        if is_ok:
            with open("Day 29 - Password Manager GUI\credentials.txt", "a") as credentials:
                credentials.write(f"{website} | {user_name} | {password}\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
        




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

#Lock logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="Day 29 - Password Manager GUI\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#Website label and button
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

#Email entry and button
userinfo_label = Label(text="Email/Username:", bg="white")
userinfo_label.grid(column=0, row= 2)

userinfo_entry = Entry(width=35)
userinfo_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
userinfo_entry.insert(0,"bryant@gmail.com")

#Password label and button
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row= 3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row= 3, sticky="EW")

#Add button and functionality
add_button = Button(text="Add", width=36, command=save_creds)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

#Generate random password button and functionality
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3, sticky="EW")



window.mainloop()