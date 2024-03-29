import pandas as pd

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())
print(len(df))

# check null values
print(df.isnull().sum())

# Drop rows which have NULL values
df = df.dropna(axis=0)

print(df.isnull().sum())
print(len(df))