
import matplotlib.pyplot as plt

temp = [20,22,24,26,28,30,32,34,36,38]
sales = [50,55,60,70,80,90,100,110,120,130]

plt.scatter(temp, sales)
plt.title("Temperature vs Ice Cream Sales")
plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.show()
