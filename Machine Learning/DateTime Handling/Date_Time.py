# to extract date features from the data
import pandas as pd
import numpy as np
import datetime

df = pd.read_csv(r'Machine Learning\DateTime\Traffic data.csv', nrows=100)
print(df.head())

# drop columns
df = df.drop(columns=['ID','Count'])

df['Datetime'] = pd.to_datetime(df['Datetime'])
print(df.head())

df['date'] = df['Datetime'].dt.date
df['time'] = df['Datetime'].dt.time
print(df.head())

# find difference from current day
df['difference'] = datetime.datetime.today() - df['Datetime']
print(df.head())