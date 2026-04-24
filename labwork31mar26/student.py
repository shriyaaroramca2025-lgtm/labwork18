
import matplotlib.pyplot as plt

days = list(range(1,11))
students = [40,42,43,45,46,48,47,49,50,52]

plt.plot(days, students)
plt.title("Student Attendance")
plt.xlabel("Day")
plt.ylabel("Students")
plt.show()
