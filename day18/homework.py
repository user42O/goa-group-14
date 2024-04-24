name = "mateo"
even_indexes_string = ''
        #  0 1 2 3 4 5
for i in range(0, len(name)):
    if i % 2 == 0:
        even_indexes_string = even_indexes_string + name[i]

print(even_indexes_string)









num = 5

# (+)
num = num + 6
num += 6

num = num + 8
num += 8

num = num + 4
num += 4

# (-)
num = num - 1
num -= 1

num = num -3
num -= 3

num = num -7
num -= 7

# (*)
num = num * 2
num *= 2

num = num * 5
num *= 5

num = num * 3
num *= 3

# (/)
num = num / 2
num /= 2

num = num / 4
num /= 4

num = num /6
num /= 6

# (%)
num = num % 6
num %= 2

num = num % 2
num %= 1

num = num % 8
num %= 4

print(num)