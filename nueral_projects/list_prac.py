# numbers = [19, 13, 41, 45, 23, 2]

# filt_list = [x for x in numbers if x % 2 == 0]

# for number in numbers:
#     if number % 2 == 0:
#         filt_list.append(number)
# print(filt_list)      

# number = [1,2,3,4,5,6,7]

# powers_of_two = [2 ** x for x in range(30)]

# print(powers_of_two)

words = ['automobile', 'car', 'anger', 'fox', 'anchor']

words = [word.upper() if word.startswith('a') else word for word in words]
print(words)
