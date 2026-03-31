import matplotlib.pyplot as plt

activities = ["Study", "Sleep", "Exercise", "Entertainment"]
time_spent = [6, 8, 2, 4]

explode = (0.1, 0, 0, 0)  # Explode "Study"

plt.pie(time_spent, labels=activities, autopct='%1.1f%%',
        explode=explode, startangle=90)

plt.title("Daily Time Distribution")
plt.show()
