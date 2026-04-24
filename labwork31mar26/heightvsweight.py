
import matplotlib.pyplot as plt

height = [150,155,160,165,170,175,180,185,190,195]
weight = [50,52,55,58,60,65,70,75,80,85]

plt.scatter(height, weight)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()
