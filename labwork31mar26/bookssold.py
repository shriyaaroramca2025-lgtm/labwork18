
import matplotlib.pyplot as plt

books = ['Math','Science','English','History','Geography']
sales = [120,150,130,90,80]

plt.bar(books, sales)
plt.title("Books Sold")
plt.xlabel("Books")
plt.ylabel("Sales")
plt.show()
