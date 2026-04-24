import matplotlib.pyplot as plt

cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
population = [19000000, 20000000, 15000000, 11000000, 13000000]

plt.barh(cities, population, color='teal')

plt.title("Population of Cities")
plt.xlabel("Population")
plt.ylabel("Cities")

plt.show()
