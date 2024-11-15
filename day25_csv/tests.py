# with open('day25_csv/weather_data.csv') as weather_file:
#     weather_data = weather_file.readlines()
# print(weather_data)

# import csv

# with open('day25_csv/weather_data.csv') as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
        
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# temperatures = data['temp']

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)
# print(f"The average of temperature is {temperatures.mean()}")
# print(f"The maximum temperature is {temperatures.max()}")

# #Get column data
# data['condition']
# data.condition

#Get row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((9/5*monday.temp)+32)

#Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# our_data = pandas.DataFrame(data_dict)
# our_data.to_csv('new_data.csv')
# print(our_data)

df = pandas.read_csv('squirrel_data.csv')
all_colors = df['Primary Fur Color']
gray = all_colors[all_colors == 'Gray'].count()
cinnamon = all_colors[all_colors == 'Cinnamon'].count()
black = all_colors[all_colors == 'Black'].count()

squirrel_data = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray, cinnamon, black]
}

squirrel_count = pandas.DataFrame(squirrel_data)
squirrel_count.to_csv('squirrel_count.csv')