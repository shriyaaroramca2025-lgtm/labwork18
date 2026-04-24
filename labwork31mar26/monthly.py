
import matplotlib.pyplot as plt

categories = ['Food','Rent','Travel','Shopping','Bills']
amount = [5000,12000,3000,4000,2500]

plt.bar(categories, amount)
plt.title("Monthly Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()
