
import matplotlib.pyplot as plt

apps = ['Instagram','Facebook','Twitter','Snapchat','Others']
users = [35,25,15,15,10]

plt.pie(users, labels=apps, autopct='%1.1f%%')
plt.title("Social Media Usage")
plt.show()
