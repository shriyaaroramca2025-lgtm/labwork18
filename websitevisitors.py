import matplotlib.pyplot as plt
days = list(range(1,11))
visitors = [120,135,150,165,180,200,220,210,230,240]

plt.plot(days, visitors)
plt.title("Website Visitors")
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.show()
