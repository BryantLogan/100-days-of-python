#   FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("Day 30 - Errors, Exceptions, JSON Data\\a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error that I made up.")

#   KeyError
# a_dictionary = {"key": "value"}
# value + a_dioctionary["non_existent_key"]

#   IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# frit = fruit_list[3]

#   TypeError
# text = "abc"
# print(text + 5)


###     Try, Except, Else, Finally ###
# Try: something that might cause an exception 
# Except: Do this if there was an ecveption 
# Else: Do this if there were no exceptions 
# Finally: Do this no matter what happens


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)