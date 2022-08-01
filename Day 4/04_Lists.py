# A list is a data structure

# states =    ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
#            "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
#            "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", 
#            "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", 
#            "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", 
#           "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", 
#            "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
#            "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
#            "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
#            "West Virginia", "Wisconsin", "Wyoming"]

# print(states)
# print(states[0:26])

# states[1] = "Alasqua" #adds list item to position
# states.append("Bryantland") #adds list item to the end of the list
# states.extend(["Andrewland", "Evanscotia"]) #adds another list to the end of the list
# num_of_states = len(states)
# print(len(states))
# print(states[num_of_states - 1])


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", 
#               "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)