# small pizza = $15
# med pizza = $20
# large pizza = $25

#pepperoni for small pizza = $2, medium and large pizza = $3

#extra cheese = $1 for any size pizza

# ask what size, if they want pepperoni, and want extra cheese
#print total bill


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza would you like? S, M, L?: ")
add_pepperoni = input("Do you want to add pepperoni? Y/N: ")
extra_cheese = input("Do you want extra cheese? Y/N: ")

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill +=1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill +=1

print(f"Your total bill is ${bill}")


