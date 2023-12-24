import matplotlib.pyplot as plt
import numpy as np

# python = (85, 67, 23, 98)
# java = (50, 67, 89, 14)
# networking = (60, 20, 56, 22)
# machine_learning = (88, 23, 40, 87)
#
# people = ['Bob', 'Anna', 'John', 'Mark']
#
# index = np.arange(4)
# bar_width = 0.2
#
# plt.bar(index, python, width=bar_width, label="Python")
# plt.bar(index + bar_width, java, width=bar_width, label="Java")
# plt.bar(index + 2 * bar_width, networking, width=bar_width, label="Networking")
# plt.bar(index + 3 * bar_width, machine_learning, width=bar_width, label="Machine Learning")
#
# plt.xlabel('People')
# plt.ylabel('Scores')
# plt.title('Programming Scores by Person and Language')
# plt.xticks(index + 1.5 * bar_width, people)
#
# plt.legend()
# plt.show()

python = (85, 67, 23, 98)
java = (50, 67, 89, 14)
networking = (60, 20, 56, 22)
machine_learning = (88, 23, 40, 87)

people = ['Bob', 'Anna', 'John', 'Mark']

index = np.arange(4)
plt.bar(index, python, width=0.2, label="Python")
plt.bar(index + 0.2, java, width=0.2, label="Java")
plt.bar(index + 0.4, networking, width=0.2, label="Networking")
plt.bar(index + 0.6, machine_learning, width=0.2, label="Machine Learning")

plt.title("IT Skill Levels")
plt.xlabel("Person")
plt.ylabel("Skill Level")
plt.xticks(index + 0.2, people)
plt.legend(loc='upper left')
plt.ylim(0, 240)

plt.show()

