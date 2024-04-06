import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

df = pd.read_csv(r'Machine Learning\Handling Imbalanced Data\Oversampling\creditcard.csv', nrows=10000)
print(df.head())

X = df.drop(columns=['Class'], axis=1)
y = df['Class']

print(Counter(y))

over = SMOTE(sampling_strategy=0.1)
under = RandomUnderSampler(sampling_strategy=0.5)

pipeline = Pipeline([('o', over), ('u', under)])
X_resample, y_resample = pipeline.fit_resample(X, y)
print(Counter(y_resample))