year = int(input("Which year do you want to check? "))

if year % 4 != 0:
    print(year , " is not a leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print(year, "is not a leap year")
else:
    print(year , "is a leap year")
