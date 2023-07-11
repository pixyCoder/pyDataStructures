import pandas as pd

df1 = pd.DataFrame({"City" : ["Los Angeles", "San Francisco", "San Diego"], "Temperature" : [80.0, 65.0, 85.0]})

df2 = pd.DataFrame({"City" : ["Los Angeles", "San Francisco", "Seattle"], "Relative humidity" : [0.4, 0.2, 0.6]})

df = pd.merge(df1, df2, on="City", how="outer", indicator="True")

print()
print("Temperature dataframe")
print(df1)

print()
print("Humidity dataframe")
print(df2)

print()
print("Merged dataframe")
print(df)
