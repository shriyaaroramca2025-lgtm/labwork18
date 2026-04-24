import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct']
price = [95,96,98,99,101,103,104,102,105,106]

plt.plot(months, price)
plt.title("Fuel Price Changes")
plt.xlabel("Month")
plt.ylabel("Price")
plt.show()
