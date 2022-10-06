import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

## filter the colors ##


gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
print (gray_color_count)

red_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print (red_color_count)

black_color_count = len(data[data["Primary Fur Color"] == "Black"])
print (black_color_count)

# creating the data frame ##

data_dict = {
    "Fur Color": ["gray", "Red", "Black"],
    "Count" : [gray_color_count, red_color_count, black_color_count]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("squirrel_count.csv")

