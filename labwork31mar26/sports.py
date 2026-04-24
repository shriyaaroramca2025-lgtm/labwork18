
import matplotlib.pyplot as plt

sports = ['Cricket','Football','Tennis','Badminton','Hockey']
fans = [200,150,80,90,60]

plt.bar(sports, fans)
plt.title("Sports Popularity")
plt.xlabel("Sport")
plt.ylabel("Fans")
plt.show()
