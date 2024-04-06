"""
Data Standardization is done to have mean as 0 and lesser standard deviation for better predictions
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'Machine Learning\Outlier_handling\winequality.csv')
print(df.head())
print(df.describe())

sns.histplot(df['fixed acidity'])
plt.show()

scaled_data = df.copy()

## z-score method
# scaled_value = (value - mean) / std
# original_value = (scaled_value * std) + mean

# apply the formula
scaled_data['fixed acidity'] = (scaled_data['fixed acidity'] - scaled_data['fixed acidity'].mean()) / scaled_data['fixed acidity'].std()

sns.histplot(scaled_data['fixed acidity'])
plt.show()