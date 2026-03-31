
import matplotlib.pyplot as plt

speed = [20,30,40,50,60,70,80,90,100,110]
fuel = [15,14,13,12,11,10,9,8,7,6]

plt.scatter(speed, fuel)
plt.title("Speed vs Fuel Consumption")
plt.xlabel("Speed")
plt.ylabel("Fuel Consumption")
plt.show()

