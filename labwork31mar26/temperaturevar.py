import matplotlib.pyplot as plt
days = list(range(1,11))
temp = [28,29,30,31,32,33,31,30,29,28]

plt.plot(days, temp)
plt.title("Temperature Variation")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()
