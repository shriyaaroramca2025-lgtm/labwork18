
import matplotlib.pyplot as plt

exp = [1,2,3,4,5,6,7,8,9,10]
salary = [20000,25000,30000,40000,50000,60000,70000,80000,90000,100000]

plt.scatter(exp, salary)
plt.title("Experience vs Salary")
plt.xlabel("Experience (years)")
plt.ylabel("Salary")
plt.show()
