import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from imblearn.under_sampling import RandomUnderSampler

df = pd.read_csv(r'Machine Learning\Handling Imbalanced Data\Oversampling\creditcard.csv', nrows=1000)
print(df.head())

X = df.drop(columns=['Class'], axis=1)
y = df['Class']

print(Counter(y))

undersampler = RandomUnderSampler(sampling_strategy='majority')  # under sample the majority to equal minority
X_over, y_over = undersampler.fit_resample(X, y)
print(Counter(y_over))

undersampler = RandomUnderSampler(sampling_strategy=0.3)    # undersample the majority such that minority is 30% of majority
X_over, y_over = undersampler.fit_resample(X, y)
print(Counter(y_over))