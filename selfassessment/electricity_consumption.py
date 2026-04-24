import matplotlib.pyplot as plt

time_intervals = ["6AM", "9AM", "12PM", "3PM", "6PM", "9PM"]
consumption = [2, 5, 7, 6, 8, 4]

plt.step(time_intervals, consumption, where='mid', color='green', marker='o')

plt.title("Electricity Consumption During the Day")
plt.xlabel("Time Intervals")
plt.ylabel("Consumption (kWh)")

plt.grid(True)
plt.show()
