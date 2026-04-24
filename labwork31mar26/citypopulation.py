
import matplotlib.pyplot as plt

cities = ['Delhi','Mumbai','Bangalore','Chennai','Kolkata']
population = [20,18,12,10,14]

plt.bar(cities, population)
plt.title("City Population")
plt.xlabel("City")
plt.ylabel("Population (in lakhs/millions)")
plt.show()
