import numpy as np

def l1_norm(x) :
    x_norm = np.abs(x)
    x_norm = np.sum(x_norm)
    return x_norm

def l2_norm(x) :
    x_norm = x * x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)
    return x_norm

x = np.array([[1, 2, 3], [4, 5, 6]], float)
print(x)
print(l1_norm(x))
print(l2_norm(x))

def angle(x, y) :
    v = np.inner(x, y) / (l2_norm(x) * l2_norm(y))
    theta = np.arccos(v)
    return theta

y = np.array([[0, 1, 2] [3, 4, 5]])
print(angle(x, y))
print(np.inner(x, y))