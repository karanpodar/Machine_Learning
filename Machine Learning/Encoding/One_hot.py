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