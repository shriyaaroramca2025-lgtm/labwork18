import matplotlib.pyplot as plt

age = [18,20,22,25,28,30,32,35,38,40,42,45,48,50,55]

plt.hist(age)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
