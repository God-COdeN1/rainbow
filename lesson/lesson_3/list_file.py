cat = "cat"
cat = list(cat)
list_cat = list(cat)
print(list_cat)
list_1 = [1, 5,"str", "poshta@gmail.com"]
list_1.append(1)
list_none = []
list_all = list_none + list_1
print(list_all)
print(list_all.count(1))
item = "@"
for fn in list_all:
    if isinstance(fn, str) and item in fn:
        print(fn)

# for i in range(len(list_all)):
#     print(f"Index-{i}, Vaul-{list_all[i]}")




list24 = ["Friday", 25, 1.5, True,]
