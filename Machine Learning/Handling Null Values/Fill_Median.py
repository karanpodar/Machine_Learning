import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())

print(df['Loan_Amount_Term'].median())

# check null values
print(df.isnull().sum())

new_df = df.copy()

# fill missing value for numerical
new_df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())
print(new_df.isnull().sum())