import pandas as pd
from category_encoders import BinaryEncoder


# 0 0 - 0
# 0 1 - 1
# 1 0 - 2
# 1 1 - 3


df = pd.read_csv(r'Machine Learning\Encoding\Loan Prediction Dataset.csv')
print(df.head())
print(df.groupby('Education').size())

# fill null values
df['Education'] = df['Education'].fillna('No')
print(df.groupby('Education').size())

be = BinaryEncoder()
be_enc = be.fit_transform(df['Education'])

print(be_enc.head())