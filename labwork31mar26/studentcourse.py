
import matplotlib.pyplot as plt

courses = ['Python','Java','C++','Web','AI']
students = [40,35,25,30,20]

plt.pie(students, labels=courses, autopct='%1.1f%%')
plt.title("Course Distribution")
plt.show()