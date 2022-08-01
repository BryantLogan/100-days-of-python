print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("Great! You can ride this rollercoaster!")
    age = int(input("What is your age? "))
    if age >=18:
        bill = 12
        print("Adult tickets are $12")
    elif age >= 12 and age < 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 5
        print("Child tickets are $5")
    
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo =="Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you are not tall enough to ride :(")