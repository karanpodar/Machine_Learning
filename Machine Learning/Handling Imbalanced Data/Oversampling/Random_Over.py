import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from imblearn.over_sampling import RandomOverSampler

df = pd.read_csv(r'Machine Learning\Handling Imbalanced Data\Oversampling\creditcard.csv', nrows=1000)
print(df.head())

X = df.drop(columns=['Class'], axis=1)
y = df['Class']

print(Counter(y))

oversampler = RandomOverSampler(sampling_strategy='minority')  # oversample the minority to equal majority
X_over, y_over = oversampler.fit_resample(X, y)
print(Counter(y_over))

oversampler = RandomOverSampler(sampling_strategy=0.3)    # oversample the minority to 30% of majority
X_over, y_over = oversampler.fit_resample(X, y)
print(Counter(y_over))