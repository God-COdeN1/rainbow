# set - {}
empety_set = set()
print(type(empety_set))
print(empety_set)

set_1 = {1, 22, 22, 4, 5, 1, 4, 10, 10}
print(set_1)
list_1 = [1, 22, 22, 4, 9, 1, 8, 10, 10, 33, 33]
print(list_1)

list_to_set = set(list_1)
print(list_to_set)

set_1.add(842)
print(set_1)

set_1.update(set({842, 45, 35}))
print(set_1)

set_1.remove(45)
print(set_1)

set_1.discard(4)
print(set_1)

set_2 = {1, 2, 3, 4, 5}
set_3 = {3, 4, 5, 7, 9}

union_set = set_2.union(set_3)
all = union_set | set_1
print(all)

inters_set = set_2.intersection(set_3)
print(inters_set)
print (set_2 & set_3)

differ_set = set_2.difference(set_3)
print(differ_set)
print(set_2 - set_3)

f_set_1 = frozenset([1, 2, 3, 10])
print(type(f_set_1))
print(dir(f_set_1))
