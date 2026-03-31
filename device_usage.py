
import matplotlib.pyplot as plt

devices = ['Mobile','Laptop','Tablet','Desktop','Others']
usage = [50,25,10,10,5]

plt.pie(usage, labels=devices, autopct='%1.1f%%')
plt.title("Device Usage")
plt.show()
