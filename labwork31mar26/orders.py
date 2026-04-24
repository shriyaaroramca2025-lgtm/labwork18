
import matplotlib.pyplot as plt

days = list(range(1,11))
orders = [50,55,60,62,65,70,75,80,78,85]

plt.plot(days, orders)
plt.title("Orders Per Day")
plt.xlabel("Day")
plt.ylabel("Orders")
plt.show()
