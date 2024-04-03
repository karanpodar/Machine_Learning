# to extract time features from the data
import pandas as pd
import numpy as np

df = pd.read_csv(r'Machine Learning\DateTime\Traffic data.csv', nrows=100)
print(df.head())

# drop columns
df = df.drop(columns=['ID','Count'])

df['Datetime'] = pd.to_datetime(df['Datetime'])
print(df.head())

df['hour'] = df['Datetime'].dt.hour
df['minute'] = df['Datetime'].dt.minute
df['second'] = df['Datetime'].dt.second
print(df.sample(frac=1).head())

