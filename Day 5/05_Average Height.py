student_heights = input("Input a list of student heights ").split(", ")
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

class_size = 0
total_heights = 0

for i in student_heights:
    class_size += 1

for height in student_heights:
    total_heights += height

# print(class_size)
# print(total_heights)
# class_size = len(student_heights)
# total_heights = sum(student_heights)

average_height = total_heights / class_size
print(f"The average height in the class is: {average_height}")