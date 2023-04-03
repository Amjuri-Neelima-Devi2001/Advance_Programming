import pandas as pd
df=pd.read_csv("C://MyDataSets//tips.csv")
json=df.to_json(path_or_buf="C://MyDataSets//df.json")
print(json)
print(df)