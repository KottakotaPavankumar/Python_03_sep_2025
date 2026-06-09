import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [20, 21, None, 19, 22],
    'Gender': ['Male', 'Male', 'Female', 'Male', 'Female'],
    'Score': [85, 92, 78, None, 95],
    'Grade': ['A', 'A', 'B', 'C', 'A']
}

df = pd.DataFrame(data)
print("Pre Processed data:\n", df)

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Score'].fillna(df['Score'].median(), inplace=True)

# Encode categorical variables
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
df['Grade'] = label_encoder.fit_transform(df['Grade'])

# Define feature matrix X and target y
X = df[['Age', 'Gender', 'Score']]
y = df['Grade']

# Apply SelectKBest feature selection
X_new = SelectKBest(f_classif, k=1).fit_transform(X, y)

print("Processed Data:\n", df)
print("Selected Features (one best feature):\n", X_new)