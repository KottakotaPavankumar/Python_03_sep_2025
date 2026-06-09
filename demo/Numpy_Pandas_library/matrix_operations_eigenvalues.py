import numpy as np

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(C)

print("Matrix C:\n", C)
print("Eigenvalues:\n", eigenvalues)
