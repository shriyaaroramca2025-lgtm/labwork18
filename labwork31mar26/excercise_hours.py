
import matplotlib.pyplot as plt

hours = [1,2,3,4,5,6,7,8,9,10]
calories = [100,150,200,250,300,350,400,450,500,550]

plt.scatter(hours, calories)
plt.title("Exercise vs Calories Burned")
plt.xlabel("Hours")
plt.ylabel("Calories")
plt.show()
