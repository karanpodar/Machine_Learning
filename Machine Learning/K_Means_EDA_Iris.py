from sklearn.cluster import KMeans
from sklearn import preprocessing
from matplotlib import pyplot as plt
import seaborn as sns

iris_df = sns.load_dataset("iris")
print(iris_df.head())

# dividing data into features and labels
features = iris_df.drop(["species"], axis = 1)
labels = iris_df.filter(["species"], axis = 1)
print(features.head())
# print(labels.head())
# print(labels['species'].unique())

# training KMeans model
features = features.values
print(features)
km_model = KMeans(n_clusters=3)    
km_model.fit(features)

print(km_model)
print(km_model.labels_)

#print the data points
plt.scatter(features[:,0], features[:,1], c= km_model.labels_, cmap='rainbow' )

#print the centroids
plt.scatter(km_model.cluster_centers_[:, 0], km_model.cluster_centers_[:, 1], s=100, c='black')

plt.show()

# training KMeans on K values from 1 to 10
loss =[]
for i in range(1, 11):
    km = KMeans(n_clusters = i).fit(features)
    loss.append(km.inertia_)


#printing loss against number of clusters
plt.plot(range(1, 11), loss)
plt.title('Finding Optimal Clusters via Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('loss')
plt.show()


# converting categorical labels to numbers

le = preprocessing.LabelEncoder()
labels = le.fit_transform(labels)

#print the data points with original labels
plt.scatter(features[:,0], features[:,1], c= labels, cmap='rainbow' )

plt.show()