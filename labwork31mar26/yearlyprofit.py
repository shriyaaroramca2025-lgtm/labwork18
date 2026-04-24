import matplotlib.pyplot as plt

years = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
profit = [20,25,30,35,40,38,45,50,55,60]

plt.plot(years, profit)
plt.title("Yearly Company Profit")
plt.xlabel("Year")
plt.ylabel("Profit")
plt.show()
