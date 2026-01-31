import pandas as pd

df = pd.read_csv('data.csv')
df.fillna(0, inplace=True)
print(df.to_string())