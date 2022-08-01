import random

bankers = input("Enter the banker's names separated by a comma: ")

names = bankers.split(", ")

len_names = (len(names))

random_choice = random.randint(0, len_names - 1)

paying_person = names[random_choice]

print("The person paying for this mean is " + paying_person)
