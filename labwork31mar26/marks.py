
import matplotlib.pyplot as plt


students = ['A','B','C','D','E']
marks = [78,85,90,76,88]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
