
import matplotlib.pyplot as plt

transport = ['Bus','Train','Car','Bike','Others']
usage = [30,25,20,15,10]

plt.pie(usage, labels=transport, autopct='%1.1f%%')
plt.title("Transport Usage")
plt.show()
