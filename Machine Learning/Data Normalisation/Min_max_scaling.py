"""
Data Normalisation is done for datasets which have huge differences in the values,
like few values are in 100s and few in 10,000s
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np
warnings.filterwarnings('ignore')

df = pd.read_csv(r'Machine Learning\Outlier_handling\winequality.csv')
print(df.head())
print(df.describe())

sns.histplot(df['alcohol'])
plt.show()

# Min - Max scaling = (value - min) / (max - min)

df_temp = df.copy()
df_temp['alcohol'] = (df_temp['alcohol'] - df_temp['alcohol'].min()) / (df_temp['alcohol'].max() - df_temp['alcohol'].min())

sns.histplot(df_temp['alcohol'])
plt.show()