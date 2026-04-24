
import matplotlib.pyplot as plt

purchase = [500,700,800,1000,1200,1500,1700,2000,2200,2500,2700,3000,3200,3500,4000]

plt.hist(purchase)
plt.title("Purchase Amount")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()
