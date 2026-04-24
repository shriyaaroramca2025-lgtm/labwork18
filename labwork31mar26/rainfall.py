
import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct']
rainfall = [10,15,20,30,40,80,120,100,60,30]

plt.plot(months, rainfall)
plt.title("Rainfall (mm)")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.show()
