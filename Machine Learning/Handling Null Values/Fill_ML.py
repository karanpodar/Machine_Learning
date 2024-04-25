import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from lightgbm import LGBMRegressor

df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())

new_df = df.copy()

new_df = new_df[['LoanAmount', 'Loan_Amount_Term', 'ApplicantIncome', 'CoapplicantIncome']]
print(new_df.head())
print(new_df.isnull().sum())

col = "LoanAmount"

# fill numerical values
new_df_temp = new_df.dropna(subset=[col], axis=0)
print(col, len(new_df_temp))

# input and output split
X = new_df_temp.drop(columns=[col], axis=1)
y = new_df_temp[col]

model = LGBMRegressor(use_missing=False)
model.fit(X, y)

d = {}
temp = new_df.drop(columns=[col], axis=1)
d[col] = list(model.predict(temp))

i = 0
for val, d_val in zip(new_df[col], d[col]):
    if pd.isna(val):
        new_df.at[i, col] = d_val
        # print(d_val)
    i += 1

print(new_df.isnull().sum())

print(new_df.head())
