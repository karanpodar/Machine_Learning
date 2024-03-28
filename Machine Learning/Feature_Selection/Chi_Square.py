"""
Chi Square is for Categorical values
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2
import numpy as np

df = pd.read_csv(r'Machine Learning\Feature_Selection\Loan Prediction Dataset.csv')
df = df[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area', 'Loan_Status']]

# fill null values
for col in df.columns:
    df[col] = df[col].fillna(df[col].mode()[0])
print(df.head())

# label encoding
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
print(df.head())

X = df.drop(columns=['Loan_Status'], axis=1)
y = df['Loan_Status']

chi_scores = chi2(X, y)

print(chi_scores)

# higher the chi value, higher the importance
chi_values = pd.Series(chi_scores[0], index=X.columns)   # chi_scores[0] is the chi values
chi_values.sort_values(ascending=False, inplace=True)
chi_values.plot.bar()
plt.show()

# if p-value > 0.05, lower the importance (higher the p-value, lower the importance)
p_values = pd.Series(chi_scores[1], index=X.columns)    # chi_scores[1] is the p values
p_values.sort_values(ascending=False, inplace=True)
p_values.plot.bar()
plt.show()