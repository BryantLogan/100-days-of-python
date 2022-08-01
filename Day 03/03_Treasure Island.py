print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice_1 = input("You've come up to fork in the woods. Do you want to go left or right?\nType 'left' or 'right: ").lower()
if choice_1 != "left":
    print("You got eaten by wolves. Game over")
else:
    choice_2 = input("You've reached a river.\nDo you want to swim, or wait for a boat?\nType 'swim' or 'wait': ").lower()
    if choice_2 != "wait":
        print("The rapids carried you over a waterfall. Game over")
    else:
        choice_3 = input("You've arrived to the island, and find a cabin with two doors. Do you go through the red, blue, or yellow door?\nType 'red', 'blue', or 'yellow': ").lower()
        if choice_3 != "yellow":
            print("You fell through the floorboards. Game over")
        else:
            print("Congratulations! You found the treasure!")

