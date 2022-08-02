row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]

treasure_spot = (input("Where would you like to place the treasure?: "))

horizontal = int(treasure_spot[0])
vertical = int(treasure_spot[1])

map[vertical - 1][horizontal - 1] = "X"

# selected_row = map[vertical -1]
# selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")





