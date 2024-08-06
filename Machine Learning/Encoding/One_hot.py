'''
we convert each values to 1 and rest as 0

For ex - if we have 2 colors -red, green, yellow
We will have 1 column for each color and we will set the value as 1 in their respective column
'''

import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = sns.load_dataset("iris")
print(df.head())
print(df['species'].value_counts())

ohe = OneHotEncoder()

ohe_values = ohe.fit_transform(df[['species']]).toarray()
print(ohe_values)

ohe_df = pd.DataFrame(ohe_values)
enc_df = pd.concat([df['species'], ohe_df], axis=1).drop_duplicates()
print(enc_df.head())