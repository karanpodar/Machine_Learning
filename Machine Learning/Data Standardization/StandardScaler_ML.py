"""
Data Standardization is done to have mean as 0 and lesser standard deviation for better predictions
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv(r'Machine Learning\Outlier_handling\winequality.csv')
print(df.head())
print(df.describe())

sns.histplot(df['pH'])
plt.show()

sc = StandardScaler()

sc.fit(df[['pH']])
sc_data = sc.transform(df[['pH']])
sc_data = sc_data.reshape(-1)

sns.histplot(sc_data)
plt.show()