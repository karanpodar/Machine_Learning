import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
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

# From chi squared we got 3 features thats why using n_features_to_select=3
# we can use different classification algo for the estimator
rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=3)  # we change the features_to_select as per our requirement
rfe.fit(X, y)

for i, col in zip(range(X.shape[1]), X.columns):
    print(f"{col} selected={rfe.support_[i]} rank={rfe.ranking_[i]}")