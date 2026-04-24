
import matplotlib.pyplot as plt

langs = ['Python','Java','C++','JavaScript','Others']
popularity = [40,20,15,15,10]

plt.pie(popularity, labels=langs, autopct='%1.1f%%')
plt.title("Programming Languages")
plt.show()
