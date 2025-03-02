## Clustering

Clustering involves grouping objects or entities into clusters (groups) based on a similarity metric. In clustering we are creating categories without the help of a human teacher. Whereas, in classification, objects were assigned to categories based on the domain knowledge of a human expert. That is in classification we had human labelled examples which means the labels acted as a supervisor teaching the algorithm how to recognise various categories.

There are no labels so clustering algorithms are forced to learn representations in an unsupervised manner devoid of direct human intervention.  
       
Clustering algorithms are divided into two main groups - hard clustering algorithms and soft clustering algorithms. Hard clustering algorithms are those clustering algorithms that find clusters from data such that a data point can only belong to one cluster and no more. Soft clustering algorithms employ a technique whereby a data point may belong to more than one cluster, that is the data point is represented across the distribution of clusters using a probability estimate that assigns how likely the point belongs to one cluster or the other.

<img width="429" alt="image" src="https://github.com/user-attachments/assets/a709149e-fdf0-4fe9-a102-bce77c1574fc" />

# Introduction to Clustering
The most important input to a clustering algorithm is the distance measure. This is so because it is used to determine how similar two or more points are to each other. It forms the basis of all clustering algorithms since clustering is inherently about discriminating entities based on similarity.

There are two subgroups - **flat clustering** and **hierarchical clustering** algorithms. In flat clustering, the clusters do not share any explicit structure so there is no definite way of relating one cluster to the other like **K-means algorithm** which we would use as a case study.  

**Hierarchical clustering** algorithms first starts with each data point belonging to its own cluster, then similar data points are merged into a bigger cluster and the process continues until all data points are part of one big cluster. As a result of the process of finding clusters, there is a clear hierarchical relationship between discovered clusters.  

Flat clustering algorithms are intuitive to understand and feature linear complexity, therefore the time taken to run the algorithm increases linearly with the number of data points and because of this flat clustering algorithms scale well to massive amounts of data. As a rule of thumb, flat clustering algorithms are generally used for large datasets where a distance metric can capture similarity while hierarchical algorithms are used for smaller datasets.

**K-means** is an iterative clustering algorithm that seeks to assign data points to clusters. To run K-means algorithm, we first need to supply the number of clusters we desire to find. Next, the algorithm randomly assigns each point to a cluster and computes the cluster centroids (center of cluster). At this stage points are reassigned to new clusters based on how close they are to cluster centroids. We again recompute the cluster centroids. Finally we repeat the last two steps until no data points are being reassigned to new clusters. The algorithm has now converged and we have our final clusters.
