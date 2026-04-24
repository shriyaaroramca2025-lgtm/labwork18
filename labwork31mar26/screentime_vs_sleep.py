
import matplotlib.pyplot as plt

screen = [1,2,3,4,5,6,7,8,9,10]
sleep = [9,8.5,8,7.5,7,6.5,6,5.5,5,4.5]

plt.scatter(screen, sleep)
plt.title("Screen Time vs Sleep")
plt.xlabel("Screen Time")
plt.ylabel("Sleep Hours")
plt.show()
