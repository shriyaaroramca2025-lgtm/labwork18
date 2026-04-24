import numpy as np
matrix = np.random.randint(1, 101, (5, 5))

print("Matrix:\n", matrix)
print("Min =", matrix.min())
print("Max =", matrix.max())

'''Output-
Matrix:
 [[88 62 63 60 85]
 [ 7 95 82 23 81] 
 [10  8 93 25 75] 
 [11 46 67 35 22]
 [32 35 90 80 59]]
Min = 7
Max = 95'''