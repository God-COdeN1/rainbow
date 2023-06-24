foo1 = lambda x, y: x if x < y else y

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)

lst_to_sort.sort(reverse=True)
print(lst_to_sort)

map1 = list(map(lambda x: x * 2, lst_to_sort))
print(map1)

filter1 = lst_to_sort = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(filter1)

negative_number = range(-10, 10)
negative_numbers1 = list(filter(lambda x: x < 0, negative_number))
print(negative_numbers1)

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
same_value = list(filter(lambda x: x in list_2, list_1))
print(same_value)
