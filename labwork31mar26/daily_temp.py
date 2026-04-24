
import matplotlib.pyplot as plt

temp = [20,22,24,26,28,30,32,34,36,38,40,42,44,46,48]

plt.hist(temp)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()
