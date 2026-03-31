import matplotlib.pyplot as plt

brands = ['Samsung','Apple','Xiaomi','Oppo','Others']
share = [30,25,20,15,10]

plt.pie(share, labels=brands, autopct='%1.1f%%')
plt.title("Mobile Market Share")
plt.show()
