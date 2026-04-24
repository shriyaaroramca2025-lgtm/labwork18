import matplotlib.pyplot as plt

courses = ['Python','Java','C++','Web','AI']
students = [40,35,25,30,20]

plt.bar(courses, students)
plt.title("Students in Courses")
plt.xlabel("Course")
plt.ylabel("Students")
plt.show()
