
import matplotlib.pyplot as plt

delivery = [1,2,3,4,5,2,3,4,5,6,3,4,5,6,7]

plt.hist(delivery)
plt.title("Delivery Time")
plt.xlabel("Days")
plt.ylabel("Frequency")
plt.show()
