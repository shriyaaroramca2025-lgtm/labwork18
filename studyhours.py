import matplotlib.pyplot as plt

hours = [1,2,3,4,5,6,7,8,9,10]
marks = [40,45,50,55,60,65,70,75,85,90]

plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()
