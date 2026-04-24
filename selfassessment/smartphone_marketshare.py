import matplotlib.pyplot as plt

brands = ["Samsung", "Apple", "Xiaomi", "Oppo", "Others"]
market_share = [30, 25, 20, 15, 10]

plt.pie(market_share, labels=brands, autopct='%1.1f%%', startangle=90)

plt.title("Smartphone Market Share")
plt.show()
