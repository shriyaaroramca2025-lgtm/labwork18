
import matplotlib.pyplot as plt

categories = ['Food','Rent','Travel','Shopping','Bills']
amount = [5000,12000,3000,4000,2500]

plt.pie(amount, labels=categories, autopct='%1.1f%%')
plt.title("Monthly Expenses")
plt.show()
