import numpy as np
arr = np.random.rand(10)

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("Original Array:\n", arr)
print("Normalized Array:\n", normalized)

'''OUTPUT-Original Array:
[0.54 0.21 0.87 0.12 0.63 ...]

Normalized Array:
[0.56 0.12 0.95 0.00 0.67 ...]
'''