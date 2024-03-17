import numpy as np
import pandas as pd
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import seaborn as sns

# generating dummy data of 500 records with 4 clusters
features, labels = make_blobs(n_samples=500, centers=4, cluster_std = 2.00)

# print(features)
# print(labels)

# plotting the dummy data
# test_sc = plt.scatter(features[:,0], features[:,1])

# plt.show()

# performing kmeans clustering using KMeans class
km_model = KMeans(n_clusters=4)
print(km_model.fit(features))

#printing centroid values
# print(km_model.cluster_centers_)

#printing predicted label values
# print(km_model.labels_)

#print the data points
plt.scatter(features[:,0], features[:,1], c=km_model.labels_, cmap=('gist_rainbow')) 

#print the centroids
plt.scatter(km_model.cluster_centers_[:, 0], km_model.cluster_centers_[:, 1], s=100, c='black')
plt.show()
