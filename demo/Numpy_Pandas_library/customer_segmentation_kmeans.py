import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Sample customer data: Age, Annual Income (k$), Spending Score (1-100)
data = {
    'Age': [19, 21, 20, 23, 31, 22, 35, 40, 29, 30],
    'Income': [15, 16, 17, 20, 28, 22, 35, 40, 36, 37],
    'SpendingScore': [39, 81, 6, 77, 40, 76, 94, 41, 70, 30]
}

df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

print(df)
