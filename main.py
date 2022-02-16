#with open("weather_data.csv", "r") as file:
#    data = file.readlines()


#import csv
#
#with open("weather_data.csv", "r") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] == "temp":
#            pass
#        else:
#            temperatures.append(int(row[1]))

#    print(temperatures)


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


#my solution
#sqrl_data = pandas.DataFrame(data["Primary Fur Color"])

#sqrl_data.value_counts().to_csv("sqrl.csv")

#teacher solution

gray_squrl_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squrl_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squrl_count = len(data[data["Primary Fur Color"] == "Black"])

data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squrl_count, red_squrl_count, black_squrl_count]

}

pandas.DataFrame(data_dictionary).to_csv("sqrl2.csv")