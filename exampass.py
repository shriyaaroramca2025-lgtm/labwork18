
import matplotlib.pyplot as plt

subjects = ['Math','Science','English','History','Geography']
pass_percent = [80,75,85,70,78]

plt.bar(subjects, pass_percent)
plt.title("Exam Pass Percentage")
plt.xlabel("Subject")
plt.ylabel("Pass %")
plt.show()
