import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

churn_df = pd.read_csv(r'C:\Users\KARAN\Desktop\Python\VsCode_py\python_learn\Machine Learning\Classification\customer_churn.csv')
# print(churn_df.head())
# print(churn_df.info())

churn_df = churn_df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

numerical = churn_df.drop(['Geography', 'Gender'], axis=1)
categorical = churn_df.filter(['Geography', 'Gender'])

# print(numerical.info())
# print(categorical.info())

# print(categorical.nunique())

cat_numerical = pd.get_dummies(categorical[['Gender', 'Geography']], drop_first=False).astype(int)

# print(cat_numerical.head())

# splitting X and y
X = pd.concat([numerical, cat_numerical], axis=1).drop(['Exited'], axis=1)
# print(X.info())
# print(X.head())

y = numerical.filter(['Exited'])
# print(y.info())
# print(y.head())

# Divide Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=0)

# Data Scaling/Normalization
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform (X_test)

