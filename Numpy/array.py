import numpy as np

test_array = np.array([1, 4, 5, 8], float)
print(test_array)
print(type(test_array[0]))
print(test_array.dtype)
print(test_array.shape)
test_array_2 = np.array([[1, 4, 5, 8]], np.float32)
print(test_array_2)
print(test_array_2.shape)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(np.array(matrix, int).shape)