import numpy as np

x = np.array([[1, -2, 3], [7, 5, 0], [-2, -1, 2]])
y = np.array([[0, 1], [1, -1], [-2, 1]])

# matrix multiplication
print(x @ y)

x = np.array([[1, -2, 3], [7, 5, 0], [-2, -1, 2]])
y = np.array([[0, 1, -1], [1, -1, 0]])
print(x)
print(y)

# matrix inner product
print(np.inner(x, y))

# inverse matrix
X = np.linalg.inv(x)
print(X)
print(x @ X)
print(X @ x)

# psuedo inverse matrix
y = np.array([[0, 1], [1, -1], [-2, 1]])
Y = np.linalg.pinv(y)
print(Y @ y)
