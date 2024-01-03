def f_to_c(temp_f):
    c_temp = (temp_f - 32) * 5/9
    return c_temp
f100_in_celsius = f_to_c(int(100))
print(f100_in_celsius)