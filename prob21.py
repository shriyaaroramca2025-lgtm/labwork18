import matplotlib.pyplot as plt

categories = ['Food', 'Transport', 'Rent', 'Shopping']
values = [30, 20, 40, 10]

plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.show()
