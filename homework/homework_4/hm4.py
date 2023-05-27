x = int(input("Введіть число x: "))
squares = []  # Список для збереження квадратів
for i in range(1, x):
    square = i ** 2
    if square < x:
        squares.append(square)
print("Квадрати додатних чисел менших за", x, ":", squares)

for i in range(15, 0, -1):
    print(i)

numbers = dict(zip([1, 2, 3], ['One', 'Two', 'Three']))
print(numbers)
