import numpy as np

# Get the dimensions of the system
n = int(input("Enter the number of variables: "))
# Get the coefficient matrix
A = np.zeros((n, n))
print("Enter the coefficient matrix:")
for i in range(n):
    A[i] = list(map(float, input().split()))
# Get the constant vector
b = np.zeros(n)
print("Enter the constant vector:")
b = list(map(float, input().split()))
# Solve the linear equation Ax = b
x = np.linalg.solve(A, b)
print("Solution x:", x)
