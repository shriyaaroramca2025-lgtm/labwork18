import matplotlib.pyplot as plt
import numpy as np

# Generate random marks
marks = np.random.randint(40, 100, 100)

plt.hist(marks, bins=10, edgecolor='black')

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
