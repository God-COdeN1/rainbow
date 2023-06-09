# 1
list1 = []

# 2
list2 = ['winter', 'spring', 'summer']
list2.append('autumn')

# 2.2
spring_season = list2[1]

# 3
list3 = [1, 2, 3, 4, 5]

# 4
all_list = [list1, list2, list3]

# 5
list2[0] = 'summer'

# 6
all_list.pop(-1)

# 7
for i in range(0, 21):
    if i % 2 == 0:
        print(i)

# 8
for n in range(20, -1, -1):
    print(n)

# 9
my_tuple = (1, 'hello', True)

# 10
tuple2 = tuple(list2)
print(tuple2[-1])

# 11
a = 'yuriiwebblack@gmail.com'
for char in a:
    if char == '@':
        break
    print(char, end='')
print(" ")
# 12
a = 'yuriiwebblack@gmail.com'
for s in a:
    if s == '@' or char == '.':
        continue
    print(s, end='')