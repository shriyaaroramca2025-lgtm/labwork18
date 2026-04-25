import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

plt.scatter(x, y)

# Highlight max point
max_y = max(y)
max_x = x[y.index(max_y)]

plt.scatter(max_x, max_y)

plt.show()
