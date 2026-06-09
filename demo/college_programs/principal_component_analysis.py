import numpy as np
from sklearn.decomposition import PCA

# Principal component analysis (PCA)
X = np.random.rand(5, 3)
pca = PCA(n_components=2)
# Fit the model with X and apply the dimensionality reduction on X.
X_pca = pca.fit_transform(X)
print("Original data shape:", X.shape)
print("Set: \n", X)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Compressed data shape:", X_pca.shape)
print("Set: \n", X_pca)