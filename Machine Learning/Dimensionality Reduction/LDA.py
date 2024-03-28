"""
Linear Discriminant Analysis also works as a dimensionality reduction algorithm, it means that it reduces 
the number of dimension from original to C — 1 number of features where C is the number of classes. 
For example, we have 3 classes and 18 features, LDA will reduce from 18 features to only 2 features
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


# LDA
x_lda = LDA(n_components=2).fit_transform(X, y)
print(x_lda.shape)

plt.figure(figsize=(10,10))
sc = plt.scatter(x_lda[:, 0], x_lda[:, 1], c=y)       # c is colors
plt.legend(handles=sc.legend_elements()[0], labels=list(range(10)))
plt.show()