'''
SMOTE - Synthetic Minority Over sampling Techinique
It uses KNN algo to 
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from imblearn.over_sampling import SMOTE

df = pd.read_csv(r'Machine Learning\Handling Imbalanced Data\Oversampling\creditcard.csv')
print(df.head())

X = df.drop(columns=['Class'], axis=1)
y = df['Class']

print(Counter(y))

oversampler = SMOTE(sampling_strategy=0.5, random_state = 42)
X_over, y_over = oversampler.fit_resample(X, y)
print(Counter(y_over))