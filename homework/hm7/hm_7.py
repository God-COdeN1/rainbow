# 1
numbers = []
for x in range(10):
    numbers.append(x)

# 2
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# 3
even_numbers = []
for x in range(15):
    if x % 2 == 1:
        even_numbers.append(x)

# 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 == 1]

for number in numbers:
    if number in even_numbers:
        print(number, "is even")
    else:
        print(number, "is odd")

# 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {number: number ** 2 for number in numbers if number % 2 == 0}
print(even_squares)

# 6
email1 = input("Enter email: ")


def extract_name(email):
    return email.split("@")[0]


print(extract_name(email1))


# 7
def count_elements(*args):
    return len(args)


# 8
def vaules_to_list(**kwargs):
    values = list(kwargs.vaules())
    return values
