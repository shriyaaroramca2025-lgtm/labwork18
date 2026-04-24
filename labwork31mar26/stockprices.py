import matplotlib.pyplot as plt
days = list(range(1,11))
price = [100,102,105,108,110,107,111,115,118,120]

plt.plot(days, price)
plt.title("Stock Prices")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()
