import numpy as np

arr = np.array([10, 20, 30, 40, 50])

normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("Normalized Array:", normalized)

#output-Normalized Array: [0.   0.25 0.5  0.75 1.  ]