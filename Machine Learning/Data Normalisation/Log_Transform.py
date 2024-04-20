"""
Data Normalisation is done for datasets which have huge differences in the values, like few values are in 100s and few in 10,000s
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

sns.histplot(df['total sulfur dioxide'])
plt.show()

# Log transformation = (value - min) / (max - min)

df_temp = df.copy()
df_temp['total sulfur dioxide'] = np.log(df_temp['total sulfur dioxide']+1)  # if there is a 0 it will throw errors as log(0) = infinite, thats why adding 1 to each value

sns.histplot(df_temp['total sulfur dioxide'])
plt.show()