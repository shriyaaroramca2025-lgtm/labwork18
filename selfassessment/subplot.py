import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line Chart
axs[0, 0].plot(x, y, marker='o')
axs[0, 0].set_title("Line Chart")
axs[0, 0].set_xlabel("X-axis")
axs[0, 0].set_ylabel("Y-axis")

# Bar Chart
axs[0, 1].bar(x, y)
axs[0, 1].set_title("Bar Chart")
axs[0, 1].set_xlabel("X-axis")
axs[0, 1].set_ylabel("Y-axis")

# Pie Chart
axs[1, 0].pie(y, labels=x, autopct='%1.1f%%')
axs[1, 0].set_title("Pie Chart")

# Scatter Plot
axs[1, 1].scatter(x, y)
axs[1, 1].set_title("Scatter Plot")
axs[1, 1].set_xlabel("X-axis")
axs[1, 1].set_ylabel("Y-axis")

plt.tight_layout()
plt.show()
