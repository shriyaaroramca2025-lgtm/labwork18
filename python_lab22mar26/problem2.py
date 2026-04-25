import numpy as np
matrix = np.random.randint(1, 101, (5, 5))

print("Matrix:")
print(matrix)

print("\nMin =", matrix.min())
print("Max =", matrix.max())

'''Output:
Matrix:
[[76 14 83 11 22]
 [51 34 87 55 38]
 [ 2 43 69 29 23]
 [40 22 67 72 72]
 [85 55 86 96 20]]

Min = 2
Max = 96'''