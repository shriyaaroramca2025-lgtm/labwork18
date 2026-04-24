import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

product_A = [100, 150, 200, 250, 300, 350]
product_B = [80, 120, 160, 200, 240, 280]
product_C = [90, 140, 180, 220, 260, 300]

plt.plot(months, product_A, marker='o', label="Product A")
plt.plot(months, product_B, marker='s', label="Product B")
plt.plot(months, product_C, marker='^', label="Product C")

plt.title("Sales of Three Products")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)
plt.show()
