import pandas as pd

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())

print(df.groupby('Education').size())

col = 'Education'

# group by frequency
freq = df.groupby(col).size()/len(df)

# map the values
df.loc[:, f"{col}_freq"] = df[col].map(freq)
print(df.head())