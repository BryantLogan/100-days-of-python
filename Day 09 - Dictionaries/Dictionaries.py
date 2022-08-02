# Dictionaries have key:value pairs
# syntax {Key: Value} {"Bug": "An error in a program that prevents the program from running as expected"}
# Key: Value pairs are separated by a comma

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# will print the value of the selected key
print(programming_dictionary["Bug"])

# Adding new items to dictionary:
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Creating an empty dictionary:
empty_dictionary = {}

# Wipe an existing dictionary - good for wiping the scores after a game is over
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary:
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

####################################

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France" : {"cities_visited": ["Paris", "Lille", "Dijon"]}, 
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]},
}

# Nesting Dictionary in a List:
travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    { 
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 12
    }
]
print(travel_log)