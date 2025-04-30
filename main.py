# import pandas as pd

# dataset = pd.read_csv("archive/walmart.csv")

# print(dataset.describe())

# columns = ["Weekly_Sales", "Holiday_Flag", "Temperature", "Fuel_Price", "CPI", "Unemployment"]

# for column in columns:
#     print("Mean: ", dataset[column].mean())
#     print("Median: ", dataset[column].median())
#     print("Mode: ", dataset[column].mode())
import pandas as pd

dataset = pd.read_csv("archive/Walmart.csv")
print("Dataset loaded")

print(dataset.head())

dataset["DiscountApplied"] = False
dataset.loc[dataset["Weekly_Sales"] > 1000, "DiscountApplied"] = True
dataset.loc[dataset["Weekly_Sales"] > 1000, "Weekly_Sales"] *= 0.9

dataset.to_csv("New_Walmart.csv", index=False)
print("Changes saved to New_Walmart.csv")