import numpy as np
arr = np.random.rand(10)

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("Original Array:")
print(arr)

print("\nNormalized Array:")
print(normalized)

'''Output:
Original Array:
[0.64449866 0.85829212 0.06212042 0.72181557 0.70097168 0.00104028
 0.28188359 0.67044829 0.21908794 0.89442125]

Normalized Array:
[0.72025083 0.9595591  0.06836965 0.80679498 0.78346352 0.
 0.31436008 0.74929737 0.24407019 1.        ]'''

