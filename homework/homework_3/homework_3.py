# 1
months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May"
}

# 2
months_dict[6] = "June"

# 3
values_list = list(months_dict.values())
print(f"Значення словника: {values_list}")

# 4
keys_list = list(months_dict.keys())
print("Ключі списку: {}".format(keys_list))

# 5
items_list = list(months_dict.items())
print("Ключ значеня: %s"%(items_list))

# 6
del months_dict[1]
del months_dict[3]

# 7
another_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# 8
all_dict = months_dict.update(another_dict)

# 9
numbers_list = [12, 25, 98, 156, 36, 87]
sum = 0
for number in numbers_list:
    sum += number
print(f"Сума значень списку: {sum}")


# 10
names_list = ["Діма", "Костя", "Діна", "Влад", "Макс"]
for in_el in range(len(names_list)):
    print(f"Індекс: {in_el}, ім'я: {names_list[in_el]}")