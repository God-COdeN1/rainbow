dict_element = {
    "day": "Monday",
    "week": "First",
    "Mont": "May",
    20: 100
}

print(type(dict_element[20]))

print(id(dict_element["day"]))
list_to_dict = [[1, "Boyko"], [2, "Denisov"], [3, "Iron"]]
print(list_to_dict)
print(dict(list_to_dict))
print(dict_element)

dict_element["week"] = "Second"
print(dict_element)

dict_element["year"] = 2023
print(dict_element)

del dict_element["year"]