import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [30, 35, 50, 55, 65, 70, 80, 90]

plt.scatter(hours, marks, color='blue')

plt.title("Hours Studied vs Marks Obtained")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.grid(True)
plt.show()
