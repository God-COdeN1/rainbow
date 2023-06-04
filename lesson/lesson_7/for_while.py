# a = 0
# while a <= 10:
#     print(f"Iter, {a}")
#     a += 1
#     if a % 2 == 0:
#         print(a)
#         continue
#     print("QQQQ")
# print(a)
str_iter = 'Hello world'
list_iter = [False, 2, 3, 'hello', 50]
for i in str_iter:
    print(i)
for i in range(len(list_iter)):
    print(i, list_iter[i])

for el in enumerate(list_iter, 1):
    print(el)

list_name = ["Yurii", "Max", "Mark", "Igor"]
list_age = [25, 18, 12, 19]

for name, age in zip(list_name, sorted(list_age, reverse=True)):
    print(f'name {name}, age {age}')

print("#" * 30)
list_5 = [i**2 for i in range(0, 20 ,2)]
print(list_5)

print("#" * 30)
list_6 = {i:str(i + 2) for i in range(0, 20 ,2)}
print(list_6)


print("_"*100)

list_7 = []

for num in range(10):
    if num % 2 == 1:
        list_7.append(num ** 2)
    else:
        list_7.append(num ** 4)
print(list_7)


list_6_comperation = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_6_comperation)
