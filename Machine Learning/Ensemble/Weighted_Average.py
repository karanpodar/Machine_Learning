import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import warnings
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

df = pd.read_csv(r'Machine Learning\winequality.csv')
df = df.drop(columns=['type'], axis=1)
print(df.head())

print(df.shape)
df = df.dropna()
print(df.shape)

sns.countplot(x='quality', data=df)
plt.show()

X = df.drop(columns=['quality'], axis=1)
y = df['quality']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y) 
# stratify = yes makes sure that the percent of 0's & 1's in y_test is same as y_train

model1 = LogisticRegression()
model2 = KNeighborsClassifier()
model3 = RandomForestClassifier()

model1.fit(x_train, y_train)
model2.fit(x_train, y_train)
model3.fit(x_train, y_train)

pred1 = model1.predict_proba(x_test)
pred2 = model2.predict_proba(x_test)
pred3 = model3.predict_proba(x_test)

final_pred = (pred1*0.25+pred2*0.25+pred3*0.5)/3   # we can change weightages of each models fore better results

pred = []
for res in final_pred:
    pred.append(np.argmax(res)+3)  #from the countplot we can see the x axis starts from 3 hence adding 3, as argmax returns index values

print(accuracy_score(y_test, pred))