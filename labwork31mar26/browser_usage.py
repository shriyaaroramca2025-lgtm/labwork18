import matplotlib.pyplot as plt
browsers = ['Chrome','Firefox','Edge','Safari','Others']
usage = [60,15,10,10,5]

plt.pie(usage, labels=browsers, autopct='%1.1f%%')
plt.title("Browser Usage")
plt.show()
