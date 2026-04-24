
import matplotlib.pyplot as plt


products = ['Laptop','Mobile','Tablet','Keyboard','Mouse']
sales = [120,200,90,150,180]

plt.bar(products, sales)
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
