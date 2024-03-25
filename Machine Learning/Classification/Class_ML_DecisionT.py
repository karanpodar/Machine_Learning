import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

churn_df = pd.read_csv(r'C:\Users\KARAN\Desktop\Python\VsCode_py\python_learn\Machine Learning\Classification\customer_churn.csv')

churn_df = churn_df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

numerical = churn_df.drop(['Geography', 'Gender'], axis=1)
categorical = churn_df.filter(['Geography', 'Gender'])

cat_numerical = pd.get_dummies(categorical[['Gender', 'Geography']], drop_first=False).astype(int)

# splitting X and y
X = pd.concat([numerical, cat_numerical], axis=1).drop(['Exited'], axis=1)

y = numerical.filter(['Exited'])

# Divide Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=0)

# Data Scaling/Normalization
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform (X_test)


############## Decision tree #################

dt_clf = DecisionTreeClassifier(random_state=42, criterion='entropy', max_depth=5, min_samples_leaf=7)

classifier = dt_clf.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))