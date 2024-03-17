import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


cols = ['col1', 'col2']  
df = pd.read_csv('file_name') #reads csv 
df = pd.read_csv('file_name', names=cols)  #reads a csv file and assigns column name from cols
df.head()  #prints first 5 rows

df['column_name'].unique()  #shows unique values


for label in cols[:-1]:
    plt.hist(df[condition], color='red', label=xyz, density=True)  # plots a histogram 
    plt.title(label)   #gives the title to graph
    plt.ylabel('y-axis')  #label to y axis
    plt.xlabel('x-axis')  #label to x axis
    plt.legend()  # to show legends
    plt.show()   #to show graph

# to assign data for training, validation & testing
# 60% for training, 60-80% is for validation & 80-100% for testing
train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df))], [int(0.8*len(df))])

scaler = StandardScaler()
x = scaler.fit_transform(x)  # to standard scale the data 

data = np.hstack(x, y)  #to stack data horizontally next to each other(column stacking)

#in numpy both x & y axis should have same dimensions

#to reshape any axis 
np.reshape(y, len(y), 1)  # converts y axis (1 Dimension) to 2-D y axis

#if the data for one condition is more than another then we may need to oversample it & balance it
ros = RandomOverSampler()
X, y = ros.fit_resample(X, y)  

knn_mod = KNeighborsClassifier(n_neighbors=1)  #to call KNN model and set the number of neighbors
knn_mod.fit(X_train, y_train)  #to fit/ load the training data (small percent of sample data)

y_pred = knn_mod.predict(X_test)  #to predict the data from test values

print(classification_report(y_test, y_pred))   #to print a classification report of actual y values(y_test) and predicted values(y_predict)

