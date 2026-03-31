import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023, 2024]
profit = [20, 25, 30, 28, 35, 40]

plt.fill_between(years, profit, color='skyblue', alpha=0.5)

plt.title("Yearly Profit Growth")
plt.xlabel("Year")
plt.ylabel("Profit (in lakhs)")

plt.plot(years, profit, marker='o', color='blue')
plt.grid(True)
plt.show()
