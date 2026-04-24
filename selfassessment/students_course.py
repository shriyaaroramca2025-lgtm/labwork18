import matplotlib.pyplot as plt

courses = ["Python", "Java", "Data Science", "Web Dev"]
students = [120, 100, 80, 90]

plt.bar(courses, students, color=['blue', 'green', 'orange', 'purple'])

plt.title("Student Enrollment in Courses")
plt.xlabel("Courses")
plt.ylabel("Number of Students")

plt.show()
