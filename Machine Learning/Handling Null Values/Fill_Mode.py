"""
Mostly used for categorical data
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())

print(df['Self_Employed'].mode())

# check null values
print(df.isnull().sum())
print(df['Self_Employed'].value_counts())

sns.countplot(df['Self_Employed'])
plt.show()

new_df = df.copy()

# fill missing value for numerical
new_df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
print(new_df.isnull().sum())
print(new_df['Self_Employed'].value_counts())
sns.countplot(new_df['Self_Employed'])
plt.show()