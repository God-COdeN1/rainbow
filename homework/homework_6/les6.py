print('-' * 80)

lst1 = []
for num in range(10):
    if num % 2 == 1:
        lst1.append(num ** 2)
    else:
        lst1.append(num ** 4)
print(f'lst1 - first list {lst1}')

lst1_ = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(f'lst1 - second list {lst1_}')

print('-' * 80)

# lst2
lst2 = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(f'lst2 - first list {lst2}')

lst2_ = []
for num in range(10):
    if num % 2 == 0:
        lst2_.append(num // 2)
    else:
        lst2_.append(num * 10)
print(f'lst2 - second list {lst2_}')

print('-' * 80)

lst3 = {}
for num in range(1, 11):
    if num % 2 == 1:
        lst3[num] = num ** 2
print(f'3 - dict first {lst3}')

lst3_ = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(f'3 - dict second {lst3_}')

print('-' * 80)

lst4 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(f'4 - {lst4}')

print('-' * 80)

lst5 = {}
for x in range(10):
    if x**3 % 4 == 0:
        lst5[x] = x**3

print('-' * 80)

lst6 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        lst6[x] = x ** 3
    else:
        lst6[x] = x
print(f'6 - {lst6}')

print('-' * 80)
