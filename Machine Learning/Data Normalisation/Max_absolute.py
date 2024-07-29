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

sns.histplot(df['free sulfur dioxide'])
plt.show()

# Max absolute scaling = value / max_value

df_temp = df.copy()
df_temp['free sulfur dioxide'] = df_temp['free sulfur dioxide'] / df_temp['free sulfur dioxide'].abs().max()

sns.histplot(df_temp['free sulfur dioxide'])
plt.show()