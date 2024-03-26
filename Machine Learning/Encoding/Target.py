from category_encoders import TargetEncoder
import pandas as pd

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())
print(df.info())
print(df.nunique())

df['Loan_Status'] = df['Loan_Status'].map({'Y':1, 'N':0})
# print(df.head())

cols = ['Gender', 'Married']
target = 'Loan_Status'
for col in cols:
    te = TargetEncoder()
    # fit the data
    te.fit(X=df[col], y=df[target])
    # transform
    values = te.transform(df[col])
    df = pd.concat([df, values], axis=1)

print(df.head())    
print(df.info())