import string
print("Doing homework")
x = 15
y = 5.29
def perTriangle(sideTr):
    return sideTr * 3
def perQuadrant(sideQu1, sideQu2):
    return sideQu1 * 2 + sideQu2 * 2
while True:
    print("Input 1 for checking homework number 1 \nInput 2 for checking homework number 2 \nInput 3 for checking homework number 3")
    print("Input 4 for checking homework number 4 \nInput 5 for checking homework number 5 \nInput 6 for checking homework number 6")
    while True:
        YourNom = input("Enter num: ")
        if any(char in string.ascii_letters for char in YourNom):
            print("Must contain a digit from 1 to 3")
        elif int(YourNom) == 1:
            print("We created a variable x and set it to 15")
            print(type(x), "- here is its type")
            break
        elif int(YourNom) == 2:
            print("We created a variable y and set it to 5.29")
            print(type(y), "- here is its type")
            break
        elif int(YourNom) == 3:
            print(id(x), id(y), "- here are their places in memory")
        elif int(YourNom) == 4:
            print("7 python reserve words")
            print("if \nelse \nelif \nand \nor \nTrue \nFalse ")
            break
        elif int(YourNom) == 5:
            sideQua1 = int(input("The first side of the square: "))
            sideQua2 = int(input("The second side of the square: "))
            print(perQuadrant(sideQua1, sideQua2))
            break
        elif int(YourNom) == 6:
            sideTr = int(input("Side of the triangle: "))
            print(perTriangle(sideTr))
            break



