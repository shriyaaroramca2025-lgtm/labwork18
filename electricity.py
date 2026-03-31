import matplotlib.pyplot as plt

days = list(range(1,11))
units = [12,15,18,14,20,22,24,21,25,27]

plt.plot(days, units)
plt.title("Electricity Consumption")
plt.xlabel("Day")
plt.ylabel("Units")
plt.show()
