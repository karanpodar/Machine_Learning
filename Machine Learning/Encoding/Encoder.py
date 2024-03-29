import seaborn as sns
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

iris_df = sns.load_dataset("iris")
print(iris_df.head())
print(iris_df['species'].value_counts())

onehot = OneHotEncoder()
labelen = LabelEncoder()

iris_df['species'] = labelen.fit_transform(iris_df['species'])

print(iris_df.head())
print(iris_df['species'].value_counts())

iris_df['species'] = onehot.fit_transform(iris_df[['species']]).toarray()

print(iris_df.head())
print(iris_df['species'].value_counts())