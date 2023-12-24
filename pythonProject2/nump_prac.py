import numpy as np

# a = np.array([
#     [1, 2, 3, 7],
#     [4, 5, 6, 7],
#     [7, 8, 9, 7]
# ])
#
# b = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [70, 80, 10, 20]
# ])
#
# c = np.concatenate((a, b))
# c2 = np.stack((a, b))
#
# print(c.shape)
# print(c2.shape)

# a = a.reshape((2, 3, 2))
# print(a.flatten())

# print(a.transpose())

# for x in a.flat:
#     print(x)

# print(a.flat[7])

a = np.array([
    [1, 2, 3, 7],
    [4, 5, 6, 7],
    [7, 8, 9, 7],
    [8, 5, 3, 1]
])

# print(np.hsplit(a, 2))

b = [10, 20, 30, 40]

# a = np.append(a, [b], axis=0)

a = np.insert(a, 2, b, axis=0)
print(a)