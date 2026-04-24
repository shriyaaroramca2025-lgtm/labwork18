
import matplotlib.pyplot as plt

dept = ['HR','IT','Sales','Finance','Support']
budget = [10,30,25,15,20]

plt.pie(budget, labels=dept, autopct='%1.1f%%')
plt.title("Department Budget")
plt.show()
