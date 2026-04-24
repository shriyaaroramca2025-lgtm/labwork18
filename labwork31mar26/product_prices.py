
import matplotlib.pyplot as plt

prices = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500]

plt.hist(prices)
plt.title("Product Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
