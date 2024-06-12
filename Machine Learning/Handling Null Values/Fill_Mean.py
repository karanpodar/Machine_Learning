'''
Mostly used when the feature is in normal distribution
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())

print(df['LoanAmount'].mean())

# check null values
print(df.isnull().sum())

new_df = df.copy()

# fill missing value for numerical
new_df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())
print(new_df.isnull().sum())