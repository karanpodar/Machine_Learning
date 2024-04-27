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

# trimming - delete the outlier data
new_df = df.loc[(df['residual sugar'] <= upper_limit) & (df['residual sugar'] >= lower_limit)]
print('before removing outliers:', len(df))
print('after removing outliers:',len(new_df))
print('outliers:', len(df)-len(new_df))

sns.boxplot(new_df['residual sugar'])
plt.show()