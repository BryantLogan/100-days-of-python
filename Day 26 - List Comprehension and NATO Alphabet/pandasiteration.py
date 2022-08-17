student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#   Looping through dictionaries:
# for (key, value) in student_dict.itams():
    # print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#   Loop through data frame

# for (student, score) in student_data_frame.items():
#     print(score)

#   Loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
