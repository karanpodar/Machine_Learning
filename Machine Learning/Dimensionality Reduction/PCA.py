"""
Principal Component Analysis - PCA
"""

from keras.datasets import mnist
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings('ignore')

(X, y), (_,_) = mnist.load_data()    # _,_ is a temporary dataset usually we load train & test data from mnist  
print(X.shape, y.shape)

X = X.reshape(len(X), -1)   # converts 3D data to 2D by multipling the 2 Dimensions
print(X.shape)


# # Plotting the MNIST dataset using matplotlib
# for i in range(9):  
#     plt.subplot(330 + 1 + i)
#     plt.imshow(X[i], cmap=plt.get_cmap('gray'))
# plt.show()


# PCA
x_pca = PCA(n_components=2).fit_transform(X)
print(x_pca.shape)

plt.figure(figsize=(10,10))
sc = plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y)           # c is colors
plt.legend(handles=sc.legend_elements()[0], labels=list(range(10)))
plt.show()