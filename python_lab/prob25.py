import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
revenue = [2000, 2500, 1800, 3000, 2800]

plt.plot(months, revenue)

plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.grid()

plt.show()
