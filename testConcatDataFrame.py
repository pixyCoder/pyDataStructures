import pandas as pd

df1 = pd.DataFrame({"City" : ["Los Angeles", "San Francisco", "San Diego"], "Temperature" : [80.0, 65.0, 85.0]})

df2 = pd.DataFrame({"City" : ["Seattle", "Portland"], "Temperature" : [70.0, 75.0]})

df = pd.concat([df1, df2])

print()
print()
print('California dataframe')
print(df1)
print()
print('Rest of west coast dataframe')
print(df2)
print()
print('Concatenated dataframe')
print(df)
print()
print()
