import pandas as pd

dataset = pd.read_csv("archive/walmart.csv")

print(dataset.describe())

columns = ["Weekly_Sales", "Holiday_Flag", "Temperature", "Fuel_Price", "CPI", "Unemployment"]

for column in columns:
    print("Mean: ", dataset[column].mean())
    print("Median: ", dataset[column].median())
    print("Mode: ", dataset[column].mode())
