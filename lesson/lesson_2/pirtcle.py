""""Форматування строк"""

apple = 5
orange = 8

print("Anna has {} apples and {} oranges".format(apple, orange))
print("Anna has {1} apples and {0} oranges".format(apple, orange))
print("Anna has {big} apples and {small} oranges".format(big=apple, small=orange))
print("Anna has {0:>10} apples and {1} oranges".format(apple, orange))
print(f"Anna has {apple} apples and {orange} oranges")
print(f"Anna has %s apples and %s oranges" % (apple, orange))