# to extract date features from the data
import pandas as pd
import numpy as np

df = pd.read_csv(r'Machine Learning\DateTime\Traffic data.csv', nrows=100)
print(df.head())

# drop columns
df = df.drop(columns=['ID','Count'])

df['Datetime'] = pd.to_datetime(df['Datetime'])
print(df.head())

df['year'] = df['Datetime'].dt.year
df['month'] = df['Datetime'].dt.month
df['day'] = df['Datetime'].dt.day
df['quarter'] = df['Datetime'].dt.quarter
df['day_of_week'] = df['Datetime'].dt.dayofweek
# df['week'] = df['Datetime'].dt.week
df['is_weekend'] = np.where(df['day_of_week'].isin([5,6]), 1, 0)

print(df.head())
print(df.sample(frac=1).head(10))