
import matplotlib.pyplot as plt

duration = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75]

plt.hist(duration)
plt.title("Session Duration")
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.show()
