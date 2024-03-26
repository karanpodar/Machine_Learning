import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = sns.load_dataset("iris")
print(df.head())
print(df['species'].value_counts())

le = LabelEncoder()

df['species_label'] = le.fit_transform(df['species'])
print(df.head())

new_df = df.filter(['species', 'species_label']).drop_duplicates()
print(new_df.head())