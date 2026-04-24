import matplotlib.pyplot as plt
salary = [20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000,80000,85000,90000]

plt.hist(salary)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
