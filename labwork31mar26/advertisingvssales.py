
import matplotlib.pyplot as plt

ads = [10,20,30,40,50,60,70,80,90,100]
sales = [15,25,35,45,55,65,75,85,95,110]

plt.scatter(ads, sales)
plt.title("Advertising vs Sales")
plt.xlabel("Advertising")
plt.ylabel("Sales")
plt.show()
