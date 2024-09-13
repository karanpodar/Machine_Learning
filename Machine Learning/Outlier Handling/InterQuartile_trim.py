'''
To Detect and remove outliers using Interquantile method
Interquartile can be seen using boxplot in seaborn, it tells us the quartiles in which the data is present

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

# IQR method
q1 = df['residual sugar'].quantile(0.25)
q3 = df['residual sugar'].quantile(0.75)
iqr = q3-q1

print(q1, q3, iqr)

upper_limit = q3 + (1.5 * iqr)
lower_limit = q1 - (1.5 * iqr)
lower_limit, upper_limit

# find the outliers
df.loc[(df['residual sugar'] > upper_limit) | (df['residual sugar'] < lower_limit)]

# trimming - delete the outlier data
new_df = df.loc[(df['residual sugar'] <= upper_limit) & (df['residual sugar'] >= lower_limit)]
print('before removing outliers:', len(df))
print('after removing outliers:',len(new_df))
print('outliers:', len(df)-len(new_df))

sns.boxplot(new_df['residual sugar'])
plt.show()