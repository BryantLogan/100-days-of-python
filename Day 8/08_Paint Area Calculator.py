import math

def paint_calc(height, width, cover):
    num_paint_cans = math.ceil((test_h * test_w) / cover)
    print(f"You'll need {num_paint_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)