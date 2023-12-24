import pandas as pd
import matplotlib.pyplot as plt


series = pd.Series([10, 20, 30, 40], ['A', 'B', 'C', 'D'])

s1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
s2 = pd.Series([7, 5, 1, 2], ['a', 'b', 'c', 'd'])

# print(s1.head(6))
# print(s1.tail(2))

# def mysquare(x):
#     return x ** 2
#
# print(s1.apply(mysquare))


s1.to_csv('myseries.csv')

# s1.plot()
# plt.show()
