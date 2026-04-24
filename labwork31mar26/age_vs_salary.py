
import matplotlib.pyplot as plt

age = [22,25,28,30,35,40,45,50,55,60]
salary = [20000,25000,30000,35000,45000,55000,65000,75000,85000,95000]

plt.scatter(age, salary)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
