
import matplotlib.pyplot as plt

departments = ['HR','IT','Sales','Finance','Support']
employees = [10,30,25,15,20]

plt.bar(departments, employees)
plt.title("Department Employees")
plt.xlabel("Department")
plt.ylabel("Employees")
plt.show()
