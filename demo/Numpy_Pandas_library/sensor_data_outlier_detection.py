import numpy as np
import pandas as pd

data = {
    'Sensor1': [20, np.nan, 22, 25, 100, 23, 24, 23, np.nan, 22],
    'Sensor2': [30, 28, 29, np.nan, 35, 120, 33, 31, 30, 29]
}

df = pd.DataFrame(data)

# Fill missing values with column mean
df_filled = df.apply(lambda x: x.fillna(np.mean(x)))

# Compute Z-scores
z_scores = (df_filled - df_filled.mean()) / df_filled.std()

# Detect outliers (absolute z-score > 2)
outliers = (np.abs(z_scores) > 2)
print("Filled Data:\n", df_filled)
print("\nOutliers:\n", outliers)
