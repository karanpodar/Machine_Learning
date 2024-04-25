import pandas as pd

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())

# check null values
print(df.isnull().sum())
print(df['Gender'].value_counts())

# consider 'Prefer Not Say' as new category
df['Gender'] = df['Gender'].fillna('Prefer Not Say')

print(df['Gender'].value_counts())