import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

diagonal = np.diag(matrix)

print("Diagonal Elements:", diagonal)

#output-Diagonal Elements: [1 5 9]