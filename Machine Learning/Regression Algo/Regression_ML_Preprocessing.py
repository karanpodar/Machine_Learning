import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Preparing Data for Regression Problems

# print(sns.get_dataset_names())

tips_df = sns.load_dataset("tips")
# print(tips_df.head())
# print(tips_df.shape)

# diamond_df = sns.load_dataset("diamonds")
# print(diamond_df.head())
# print(diamond_df.shape)

# Dividing Data into Features and Labels

X = tips_df.drop(['tip'], axis=1)
y = tips_df["tip"]
# print(X.head())
# print(y.head())

# Converting Categorical Data to Numbers

numerical = X.drop(['sex', 'smoker', 'day', 'time'], axis = 1)
categorical = X.filter(['sex', 'smoker', 'day', 'time'])
# print(numerical.head())
# print(categorical.head())

# print(categorical.nunique())
# print(categorical['day'].value_counts())

# fil_values = ['Sun', 'Sat']
# fil = categorical['day'].isin(fil_values)
# print(fil)

#categorical['day'] = categorical['day'].replace({'Sat' : 'Weekend', 'Sun' : 'Weekend', 'Thur' : 'Weekday', 'Fri' : 'Weekday'})
# categorical['day'] = categorical['day'].replace({'Sat' : 0, 'Sun' : 0, 'Thur' : 1, 'Fri' : 1})
# print(categorical['day'].value_counts())

# print(numerical.isnull().value_counts())
# print(categorical.isnull().value_counts())
# print(numerical.isna().value_counts())
# print(categorical.isna().value_counts())

cat_numerical = pd.get_dummies(categorical,drop_first=False).astype(int)
# print(cat_numerical.head())

X = pd.concat([numerical, cat_numerical], axis = 1)
# X = X.replace({True: 1, False: 0})
# print(X.head())


# Divide Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=0)

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform (X_test)
