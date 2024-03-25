from sklearn.cluster import KMeans
from sklearn import preprocessing
from matplotlib import pyplot as plt
import pandas as pd

# prefix 'r' in path saves tie in loading the file
banknote_df = pd.read_csv(r'C:\Users\KARAN\Desktop\Python\VsCode_py\python_learn\Machine Learning\banknote.csv')
# print(banknote_df.head())

# print(banknote_df['class'].value_counts())

# dividing data into features and labels
features = banknote_df.drop(["class"], axis = 1)
labels = banknote_df.filter(["class"], axis = 1)
print(features.head())

# training KMeans on K values from 1 to 10
loss =[]
for i in range(1, 11):
    km = KMeans(n_clusters = i).fit(features)
    loss.append(km.inertia_)


# #printing loss against number of clusters
# plt.plot(range(1, 11), loss)
# plt.title('Finding Optimal Clusters via Elbow Method')
# plt.xlabel('Number of Clusters')
# plt.ylabel('loss')
# plt.show()

# # training KMeans with 3 clusters
# features = features.values
# km_model = KMeans(n_clusters=3)
# km_model.fit(features)

# #print the data points with predicted labels
# plt.scatter(features[:,0], features[:,1], c= km_model.labels_, cmap='rainbow' )

# #print the predicted centroids
# plt.scatter(km_model.cluster_centers_[:, 0], km_model.cluster_centers_[:, 1], s=100, c='black')

# plt.show()


# training KMeans with 2 clusters
features = features.values
km_model = KMeans(n_clusters=2)
km_model.fit(features)

# #print the data points with predicted labels
# plt.scatter(features[:,0], features[:,1], c= km_model.labels_, cmap='rainbow' )

# #print the predicted centroids
# plt.scatter(km_model.cluster_centers_[:, 0], km_model.cluster_centers_[:, 1], s=100, c='black')

# plt.show()


#print the data points with original labels
plt.scatter(features[:,0], features[:,1], c= labels.values, cmap='rainbow' )
plt.show()