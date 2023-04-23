import string
x = 15
y = 5.29
def perimeter(side1, side2, side3):
    return side1 + side2 + side3
while True:
    print("Doing homework")
    CheckNom1 = True
    print("Input 1 for checking homework number 1 \nInput 2 for checking homework number 2 \nInput 3 for checking homework number 3")
    while CheckNom1:
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
            side1 = int(input("Write the numbers with ,: "))
            side2 = int(input("Write the numbers with ,: "))
            side3 = int(input("Write the numbers with ,: "))
            print(perimeter(side1, side2, side3))
            break


