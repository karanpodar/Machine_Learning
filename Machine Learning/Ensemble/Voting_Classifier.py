import pandas as pd
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import sklearn
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv(r'Machine Learning\winequality.csv')
df = df.drop(columns=['type'], axis=1)
print(df.head())

print(df.shape)
df = df.dropna()
print(df.shape)

X = df.drop(columns=['quality'], axis=1)
y = df['quality']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y) 
# stratify = yes makes sure that the percent of 0's & 1's in y_test is same as y_train

model1 = LogisticRegression()
model2 = KNeighborsClassifier()
model3 = RandomForestClassifier()

model = VotingClassifier(estimators=[('lr', model1), ('kn', model2), ('rf', model3)], voting='soft') # soft- probability score, hard- take the majority class
model.fit(x_train, y_train)
print(model.score(x_test, y_test))  # Accuracy score
