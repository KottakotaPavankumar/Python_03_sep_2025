import numpy as np
import pandas as pd

data = {
    'Math': [90, 80, np.nan, 70, 60],
    'Physics': [85, np.nan, np.nan, 75, 65],
    'Chemistry': [np.nan, 78, 88, 68, 58]
}

df = pd.DataFrame(data)

# Fill missing values with column mean
df_filled = df.apply(lambda col: col.fillna(np.mean(col)))

print("Filled DataFrame:\n", df_filled)

# Summary statistics
summary = df_filled.describe()
print("\nSummary Statistics:\n", summary)
