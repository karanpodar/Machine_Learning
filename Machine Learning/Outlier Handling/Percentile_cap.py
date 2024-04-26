'''
To Detect and remove outliers using percentile method, which divides the data based on percentages
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np
warnings.filterwarnings('ignore')

df = pd.read_csv(r'Machine Learning\Outlier_handling\winequality.csv')
# print(df.head())
# print(df.info())
# print(df.describe())

# # to see outliers clearly
# sns.boxplot(df['residual sugar'])
# plt.show()

# find the limits
upper_limit = df['residual sugar'].quantile(0.99)
lower_limit = df['residual sugar'].quantile(0.01)
print('upper limit:', upper_limit)
print('lower limit:', lower_limit)

# find the outliers
df.loc[(df['residual sugar'] > upper_limit) | (df['residual sugar'] < lower_limit)]

# capping - change the outlier values to upper (or) lower limit values
new_df = df.copy()
new_df.loc[(new_df['residual sugar']>upper_limit), 'residual sugar'] = upper_limit
new_df.loc[(new_df['residual sugar']<lower_limit), 'residual sugar'] = lower_limit

sns.boxplot(new_df['residual sugar'])
plt.show()