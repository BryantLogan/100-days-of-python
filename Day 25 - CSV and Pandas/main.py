# with open("Day 25 - CSV and Pandas\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day 25 - CSV and Pandas\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)
            
import pandas

# data = pandas.read_csv("Day 25 - CSV and Pandas\weather_data.csv")
# print(type(data))
# print(data["temp"])
# temp_total = 0
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())

# # get data in columns
# print(data["condition"])
# print(data.condition)

# get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = (monday_temp * (9/5) + 32)
# print(monday_temp_f)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")

