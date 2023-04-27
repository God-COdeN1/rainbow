import string
import math
ex = True
print("Doing homework")
x = 15
y = 5.29
def perTriangle(sideTr):
    return sideTr * 3
def perQuadrant(sideQu1, sideQu2):
    return sideQu1 * 2 + sideQu2 * 2
def area():
    semi_p = (side_a1 + side_a2 + side_a3) / 2
    return math.sqrt(semi_p * (semi_p - side_a1) * (semi_p - side_a2) * (semi_p - side_a3))
while ex:
    print("Input 1 for checking homework number 1 \nInput 2 for checking homework number 2 \nInput 3 for checking homework number 3")
    print("Input 4 for checking homework number 4 \nInput 5 for checking homework number 5 \nInput 6 for checking homework number 6")
    print("Input 7 for checking homework number 7 \nInput 8 for checking homework number 8 \nInput 9 for checking homework number 9")
    print("Input 10 for checking homework number 10")
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
        elif int(YourNom) == 7:
            num1 = 24
            num2 = 4
            print("We created variables num1 and num2, and gave them the numbers 24 and 4")
            print(num1 / num2, "division without a quotient")
        elif int(YourNom) == 8:
            num3 = 20
            num4 = 8
            print("We created variables num3 and num4, and gave them the numbers 27 and 8")
            print(num3 / num4, "division with a quotient")
            print(num3 // num4, "- division without remainder")
            print(num3 % num4, "- the remainder after division")
        elif int(YourNom) == 9:
            letters = "abcdefghijklmnopqrstuvwxyz"
            first_letter = letters[0]
            last_letter = letters[-1]
            print(first_letter, "- first letter")
            print(last_letter, "- last letter")
        elif int(YourNom) == 10:
            side_a1 = int(input("Lead the first side: "))
            side_a2 = int(input("Lead the second side: "))
            side_a3 = int(input("Lead the third side: "))
            print(area(), "- area of a triangle")
            break
    while True:
        rest = int(input("Press 1 to exit or 2 to restart: "))
        if rest == 1:
            ex = False
            break
        elif rest == 2:
            ex = True
            break
        elif rest != 1 or 2:
            print("Enter 1 or 2!")
