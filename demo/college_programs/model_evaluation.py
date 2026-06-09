from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
knn = KNeighborsClassifier(n_neighbors=9)
scores = cross_val_score(knn, iris.data, iris.target, cv=4)
print("Cross-validation scores:", scores)
avg_score = scores.mean()
print("Average score:", avg_score)