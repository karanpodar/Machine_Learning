import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
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

############### ML using Linear Regression Algorithm ################

lin_reg = LinearRegression()
regressor = lin_reg.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('Square root Score:', np.sqrt(metrics.r2_score(y_test, y_pred)))

print(regressor.coef_) # slope of the model
print(regressor.intercept_)  # constant