#   new_list = [new_item for item in list]

# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     new_list.append(n + 1)
# print(new_list)

# OR with List comprehension:
# new_list = [n + 1 for n in numbers]
# print(new_list)

#   Sequences: list, string, tuple, range
# name = "Bryant"
# new_list = [letter for letter in name]
# print(new_list)

# new_numbers = [number *2 for number in range(1,5)]
# print(new_numbers)

# names = ["alex", "Beth", "caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) <= 4]
# cap_names = [name.upper() for name in names if len(name) >= 5]
# print(short_names)
# print(cap_names)

#   Use list comprehension to create a new list called squared_numbers. This new list should contain
#   every number in the list numbers but each number should be squared

# numbers = [1, 1, 2, 3, 5, 6, 13, 21, 34, 55]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

#   You are going to write a List Comprehension to create a new list called result. This new list should only contain 
#   the even numbers from the list numbers.

#   DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result =[num for num in numbers if num % 2 == 0]
# print(result)

#   Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#   You are going to create a list called result which contains the numbers that are common in both files.

with open("Day 26 - List Comprehension and NATO Alphabet\\file1.txt") as file_1:
    contents_1 = file_1.readlines()
with open("Day 26 - List Comprehension and NATO Alphabet\\file2.txt") as file_2:
    contents_2 = file_2.readlines()
result = [int(num.strip()) for num in contents_1 if num in contents_2]
print(result)

#   Apply list comprehension to US States Game