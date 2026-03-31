
import matplotlib.pyplot as plt

distance = [5,10,15,20,25,30,35,40,45,50]
time = [10,20,30,40,50,60,70,80,90,100]

plt.scatter(distance, time)
plt.title("Distance vs Travel Time")
plt.xlabel("Distance")
plt.ylabel("Time")
plt.show()
