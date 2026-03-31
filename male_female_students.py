import matplotlib.pyplot as plt

departments = ["CSE", "ECE", "ME", "CE"]

male_students = [60, 50, 70, 40]
female_students = [40, 60, 30, 50]

plt.bar(departments, male_students, label="Male", color='blue')
plt.bar(departments, female_students, bottom=male_students, label="Female", color='pink')

plt.title("Male and Female Students in Departments")
plt.xlabel("Departments")
plt.ylabel("Number of Students")

plt.legend()
plt.show()
