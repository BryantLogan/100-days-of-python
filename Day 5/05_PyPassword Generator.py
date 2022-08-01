import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

rand_letters = []
rand_numbers= []
rand_symbols = []

rand_password = []

for l in range (0, nr_letters):
    rand_letters += (random.choice(letters))
for n in range (0, nr_numbers):
    rand_numbers += (random.choice(numbers))
for s in range (0, nr_symbols):
    rand_symbols += (random.choice(symbols))

rand_password_list = [rand_letters, rand_numbers, rand_symbols]

for p in rand_password_list:
    rand_password += p

random.shuffle(rand_password)
final_password = "".join(rand_password)

#print(rand_password)
print(f"Your password is: {final_password}")