
import matplotlib.pyplot as plt

appliances = ['AC','Fan','Light','TV','Others']
usage = [40,20,15,15,10]

plt.pie(usage, labels=appliances, autopct='%1.1f%%')
plt.title("Electricity Usage")
plt.show()
