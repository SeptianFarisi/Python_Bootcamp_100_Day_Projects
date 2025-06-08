# with open("weather_data.csv") as data:
#     data_weather = data.readlines()
#     print(data_weather)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatur = []
#     for row in data:
#         for line in data:
#             temperatur.append(int(line[1]))
#             print(temperatur)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = data["temp"].mean()
# print(average)
#
# max = data["temp"].max()
# print(max)

# print(data[data["temp"] == data.temp.max()])

# def fahrenheit(celcius):
#     return (celcius * 9/5) + 32
#
# monday = data[data.day == "Monday"]
# monday["temp"] = fahrenheit(monday["temp"])
# print(monday)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())
data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [2473, 392, 103]
}
new_data = pd.DataFrame(data_dict)
new_data.to_csv("new_data.csv")