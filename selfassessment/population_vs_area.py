import matplotlib.pyplot as plt

cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]

population = [190, 200, 150, 110, 130]   # in lakhs
area = [1484, 603, 205, 426, 709]        # in sq km
gdp = [300, 250, 150, 180, 220]          # GDP factor

# Increase bubble size for better visibility
bubble_size = [g * 20 for g in gdp]

plt.scatter(area, population, s=bubble_size, alpha=0.6, edgecolors='black')

# Add labels slightly shifted to avoid overlap
for i in range(len(cities)):
    plt.text(area[i] + 10, population[i] + 2, cities[i])

plt.title("Population vs Area (Bubble size = GDP)")
plt.xlabel("Area (sq km)")
plt.ylabel("Population (in lakhs)")

plt.grid(True)
plt.show()

