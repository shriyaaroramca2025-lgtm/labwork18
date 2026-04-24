import matplotlib.pyplot as plt

dept_A = [30, 35, 40, 45, 50]
dept_B = [25, 30, 35, 40, 45]
dept_C = [20, 25, 30, 35, 40]

data = [dept_A, dept_B, dept_C]

plt.boxplot(data, labels=["Dept A", "Dept B", "Dept C"])

plt.title("Salary Distribution in Departments")
plt.xlabel("Departments")
plt.ylabel("Salary (in thousands)")

plt.show()
