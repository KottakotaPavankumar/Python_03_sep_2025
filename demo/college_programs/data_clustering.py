import numpy as np
from sklearn.cluster import KMeans

num_clusters = int(input("Enter the number of clusters: "))
num_points = int(input("Enter the number of data points: "))
print("Enter the data points (format: x y):")
X = []
for i in range(num_points):
    x, y = map(float, input().split())
    X.append([x, y])  # Fixed: Indentation moved inside loop

X = np.array(X)
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
kmeans.fit(X)
print("Cluster Labels:", kmeans.labels_)
print("Cluster Centers:\n", kmeans.cluster_centers_)