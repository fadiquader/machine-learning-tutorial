import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

dataset = pd.read_csv('datasets/iris.csv')
dataset.head()

x = dataset.drop(columns=['Id', 'Species'], axis=1)
x = x.values # select values and convert dataframe to numpy array

# sum of sqaured error
wcss  = [] # Array to hold sum of squared distances within clusters

for i in range(1, 11):
    # run k-means for 10 iterations with n_clusters ranging from 1 to 10
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

# plotting the result allowing us to observe `the elbow`
plt.plot(range(1, 11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Within Cluster Sum of Squares') # within cluster sum of squares
plt.show()
# we observe that the optimal value of k is 3

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(x)

# visualising the clusters
# Plot the data points that belong to the first cluster (cluster 0) in red.
# This selects the first feature (column 0) of the data points that belong to the first cluster (where y_kmeans == 0).
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Iris-setosa')
# Plot the data points that belong to the second cluster (cluster 1) in blue.
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Iris-versicolour')
# Plot the data points that belong to the third cluster (cluster 2) in green.
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')

# plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'Centroids')
plt.legend()
plt.show()

# The yellow point indicates the centroids which is at the center of each cluster.