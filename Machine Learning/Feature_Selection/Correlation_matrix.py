"""
Correlation matrix is for numerical values
We will be predicting 'cnt' column, so we need to see other features which have higher correlation with it
For feature 'temp' and 'atemp' we can see high correlation so we can drop either of it
Similarly for feature 'yr' and 'instant' we can see high correlation so we can drop either of it
Similarly for feature 'mnth' and 'season' we can see high correlation so we can drop either of it
if corr value is less than -0.05 & 0.05 we can drop those features (p-value logic)
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as nps

df = pd.read_csv(r'Machine Learning\Cross_Validation\bike sharing dataset.csv')
print(df.head())

corr = df.corr(numeric_only = True)
print(corr)

# display correlation matrix in heatmap
plt.figure(figsize=(14,9))    # to increase the size of the map
sns.heatmap(corr, annot=True, cmap='coolwarm')   # annot will display the values in the heatmap as well
plt.show()