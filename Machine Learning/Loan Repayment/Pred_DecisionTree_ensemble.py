'''
Predicts whether the bank should approves the loan of an applicant based on his profit using Ensemble Learning Methods.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import warnings
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics  import  accuracy_score , precision_score , recall_score,confusion_matrix,classification_report

warnings.filterwarnings('ignore')
kFold = StratifiedKFold(n_splits=10)

df = pd.read_csv(r"Machine Learning\Loan Repayment\loan_data.csv")
print(df.head())
print(df.shape)
print(df.info())

# to check if any null values
print(df.isnull().sum())

# to check the count of each unique values
print(df['purpose'].value_counts())

# to label encode
df['purpose']=LabelEncoder().fit_transform(df['purpose'])


# # data visualisation 
# sns.set_style('darkgrid')
# plt.hist(df['fico'].loc[df['credit.policy']==1], bins=30, label='Credit.Policy=1')
# plt.hist(df['fico'].loc[df['credit.policy']==0], bins=30, label='Credit.Policy=0')
# plt.legend()
# plt.xlabel('FICO')

# plt.show()

# plt.figure(figsize=(10,6))
# df[df['not.fully.paid']==1]['fico'].hist(bins=30, alpha=0.5, color='blue', label='not.fully.paid=1')
# df[df['not.fully.paid']==0]['fico'].hist(bins=30, alpha=0.5, color='green', label='not.fully.paid=0')
# plt.legend()
# plt.xlabel('FICO')

# plt.show()

# #creating a countplot to see the counts of purpose of loans by not.fully.paid
# plt.figure(figsize=(12,6))
# sns.countplot(data=df, x='purpose', hue='not.fully.paid')

# plt.show()

# #checking the trend between FICO and the interest rate
# plt.figure(figsize=(10,6))
# sns.jointplot(x='fico', y='int.rate', data=df)

# plt.show()

# #understanding the relationship between credit.policy and not.fully.paid
# sns.lmplot(data=df, x='fico', y='int.rate', hue='credit.policy', col='not.fully.paid', palette='Set2')

# plt.show()

# # see the correlation between the features
# plt.figure(figsize = (20, 15)) 
# sns.heatmap(df.corr(), cmap='BuPu', annot=True)

# plt.show()


# Dropping target class
X = df.drop('not.fully.paid',axis=1)
y = df['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)

# # Decision Tree

# dt_clf = DecisionTreeClassifier()
# param_grid = {'max_depth': [2,3,4,5,6,7,8,9,10,11,13,15,20]}

# grid_search = GridSearchCV(dt_clf, param_grid, scoring = 'recall_weighted',cv=kFold, return_train_score=True)
# grid_search.fit(X_train,y_train)

# print(grid_search)
# print(grid_search.best_params_)

dt_clf = DecisionTreeClassifier(max_depth=2)
# dt_clf.fit(X_train, y_train)
# y_pred_train = dt_clf.predict(X_train)
# y_pred_test = dt_clf.predict(X_test)

# train_accuracy = accuracy_score(y_train, y_pred_train)
# test_accuracy = accuracy_score(y_test, y_pred_test)

# print("Confusion Matrix \n",confusion_matrix(y_test,y_pred_test))
# print("\n")
# print("<-------------------Classification Report---------------------->\n")
# print(classification_report(y_test,y_pred_test))
# print("\n")
# print("<---------------Accuracy Scores------------------->\n")
# print('Train Accuracy score: ',train_accuracy)
# print('Test Accuracy score:',test_accuracy)

# Bagging with Decision Tree

from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import cross_val_score

scaler=StandardScaler()

# X_scaled = scaler.fit_transform(X)
# bag_dt = BaggingClassifier(dt_clf,n_estimators=100,bootstrap=True)
# score = cross_val_score(estimator=bag_dt, X=X_scaled, y=y, scoring='recall_weighted', cv=kFold, n_jobs=-1)

# print('Mean score:', score.mean())

# ADABoost with Decision tree

from sklearn.ensemble import AdaBoostClassifier

adaboost_clf = AdaBoostClassifier(dt_clf,learning_rate = 0.5)
adaboost_clf.fit(X_train, y_train)
print('Train score: {0:0.2f}'.format(adaboost_clf.score(X_train, y_train)))
print('Test score: {0:0.2f}'.format(adaboost_clf.score(X_test, y_test)))