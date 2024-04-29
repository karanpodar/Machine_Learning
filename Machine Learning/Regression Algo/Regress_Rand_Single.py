import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

############### Preprocessing from Regression_ML_Preprocessing ################
tips_df = sns.load_dataset("tips")

X = tips_df.drop(['tip'], axis=1)
y = tips_df["tip"]

numerical = X.drop(['sex', 'smoker', 'day', 'time'], axis = 1)
categorical = X.filter(['sex', 'smoker', 'day', 'time'])

cat_numerical = pd.get_dummies(categorical,drop_first=False).astype(int)

X = pd.concat([numerical, cat_numerical], axis = 1)


# Divide Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=0)

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform (X_test)

############### ML using Random Forest Algorithm to predict value for 1 input ################

rf_reg = RandomForestRegressor(random_state=42, n_estimators=500)
regressor = rf_reg.fit(X_train, y_train)

single_record = sc.transform (X.values[100].reshape(1, -1))
predicted_tip = regressor.predict(single_record)
print(predicted_tip)