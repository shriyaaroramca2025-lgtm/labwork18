import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [200, 250, 300, 280, 350, 400, 420, 390, 370, 450, 480, 500]

plt.plot(months, sales, marker='o', linestyle='-', color='blue')

plt.title("Monthly Sales of Company")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.grid(True)
plt.show()
