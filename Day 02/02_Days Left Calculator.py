age = int(input("What is your current age? "))
years_left = int(90 - age)
months_left = int(years_left * 12)
weeks_left = int(years_left * 52)
days_left = int(weeks_left * 7)

print("You have " + str(days_left) + " days, " + str(weeks_left) + " weeks, " + str(months_left) + " months left until you're 90 years old.")