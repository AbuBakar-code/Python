# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

# data = pd.read_csv('weather_data.csv')
# print(data)
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()

# print(data['temp'].mean())

# print(data['temp'].max())

# print(data.condition)

# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# temp_to_farenhite = (monday_temp * 9/5) + 32
# print(temp_to_farenhite)

# how to create a dataframe and save it as a new file

# data_dict = {
#     "students": ['abuakar', 'james', 'ron'],
#     "score" : [90, 89, 87]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("New_data")  

data = pd.read_csv('squirrel_data.csv')

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])

cinammon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

black_count = len(data[data['Primary Fur Color'] == 'Black'])


data_dict = {
    'Fur color': ['Gray', 'Red', 'Black'],
    'Count': [gray_count, cinammon_count, black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")