import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score

warnings.filterwarnings('ignore')

df = pd.read_csv(r'Machine Learning\Cross_Validation\bike sharing dataset.csv')
print(df.head())

df = df.drop(columns=['instant', 'dteday', 'casual', 'registered'], axis=1)
print(df.head())

X = df.drop(columns=['cnt'], axis=1)
y = df['cnt']

cv = KFold(n_splits=5, random_state=42, shuffle=True)
model = RandomForestRegressor()
scores = cross_val_score(model, X, y, cv=cv, n_jobs=-1)     # cv is cross validation
print(f"Error Mean: {np.mean(scores)} Error Std: {np.std(scores)}")