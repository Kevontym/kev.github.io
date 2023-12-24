import matplotlib.pyplot as plt


nationalities = ['American', 'German', 'French', 'Other']
students = [60, 23, 21, 34]


pairs = zip(students, nationalities)
pairs = sorted(list(pairs))
students, nationalities = zip(*pairs)

plt.pie(students, labels=nationalities, autopct='%.2f%%', counterclock=False, startangle=90)
plt.title("Student Nationality")
plt.show()