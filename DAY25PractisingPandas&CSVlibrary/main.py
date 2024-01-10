"""INTRODUCTION TO PANDAS AND CSV"""

# import pandas
#
# data = pandas.read_csv("C:\Desktop\Downloads\day-25-start\weather_data.csv")
# print(data)
#
# import csv
#
# with open("C:\Desktop\Downloads\day-25-start\weather_data.csv") as data_file:
#     weather_data = csv.reader(data_file)
#     temperatures = []
#     for data in weather_data:
#         if data[1] != "temp":
#             temperatures.append(data[1])
#     print(temperatures)

"""SQUIRREL COUNT"""

import pandas
import csv
data = pandas.read_csv("C:/Desktop/Downloads/2018_Squirrel_Data.csv")

# with open("C:/Desktop/Downloads/2018_Squirrel_Data.csv") as data_file:
#     squirrel_data = csv.reader(data_file)
#     squirrel_list = []
#     for data in squirrel_data:
#         if data[9] != "Highlight Fur Color":
#             squirrel_list.append(data[9])
#         print(squirrel_list)


grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
