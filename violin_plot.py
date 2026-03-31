import matplotlib.pyplot as plt
import numpy as np

class_A = np.random.randint(50, 100, 50)
class_B = np.random.randint(40, 95, 50)
class_C = np.random.randint(60, 100, 50)

data = [class_A, class_B, class_C]

plt.violinplot(data)

plt.title("Distribution of Exam Scores")
plt.xlabel("Classes")
plt.ylabel("Scores")

plt.xticks([1, 2, 3], ["Class A", "Class B", "Class C"])

plt.show()
