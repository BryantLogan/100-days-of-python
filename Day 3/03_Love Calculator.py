print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t = lower_name1.count("t")
r = lower_name1.count("r")
u = lower_name1.count("u")
e =lower_name1.count("e")

true = t + r + u + e

l = lower_name2.count("l")
o = lower_name2.count("o")
v = lower_name2.count("v")
e = lower_name2.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))


if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}. You go together like coke and Mentos.")
elif love_score >= 40 and love_score <= 50:
    print (f"Your score is {love_score}. You are alright together")
else:
    print(f"Your score is {love_score}")


# x < 10 or >90:
# Your score is x, you go together like coke and mentos

# x >= 4 and <= 50
# Your score is y, you are alright together

#else
# Your score is x