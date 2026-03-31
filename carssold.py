
import matplotlib.pyplot as plt

brands = ['Toyota','Honda','Hyundai','Kia','Ford']
sales = [100,80,90,70,60]

plt.bar(brands, sales)
plt.title("Cars Sold")
plt.xlabel("Brand")
plt.ylabel("Sales")
plt.show()
