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
    print("Input 1 (create a variable with an integer) \nInput 2 (creating a variable with a floating point) \nInput 3 (display a place in the memory of previously created changes)")
    print("Input 4 (7 reserve words in Python) \nInput 5 (rectangle perimeter) \nInput 6 (calculate the perimeter of an equilateral triangle)")
    print("Input 7 (integer division) \nInput 8 (an example with the remainder of division, set text = 'Hello' and multiplied 'Hello' 10 times) \nInput 9 (set the letters variable containing the alphabet, get the first and last letters from the letters)")
    print("Input 10 (determine the area of the triangle using Heron's formula)")
    while True:
        YourNom = input("Enter num: ")
        if YourNom in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            if YourNom == "1":
                print("We created a variable x and set it to 15")
                print(type(x), "- here is its type")
                break
            elif YourNom == "2":
                print("We created a variable y and set it to 5.29")
                print(type(y), "- here is its type")
                break
            elif YourNom == "3":
                print(id(x), id(y), "- here are their places in memory")
                break
            elif YourNom == "4":
                print("7 python reserve words")
                print("if \nelse \nelif \nand \nor \nTrue \nFalse ")
                break
            elif YourNom == "5":
                while True:
                    try:
                        sideQua1 = int(input("The first side of the square: "))
                        sideQua2 = int(input("The second side of the square: "))
                        print(perQuadrant(sideQua1, sideQua2), "- rectangle perimeter")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                break
            elif YourNom == "6":
                while True:
                    try:
                        sideTr = int(input("Side of the triangle: "))
                        print(perTriangle(sideTr), "- perimeter of an equilateral triangle")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                break
            elif YourNom == "7":
                num1 = 24
                num2 = 4
                print("We created variables num1 and num2, and gave them the numbers 24 and 4")
                print(num1 / num2, "- division without a quotient")
                break
            elif YourNom == "8":
                num3 = 20
                num4 = 8
                strin = "Hello"
                print("We created variables num3 and num4, and gave them the numbers 27 and 8")
                print("Create a string variable, name it 'Hello' and multiply it 10 times")
                print(num3 / num4, "division with a quotient")
                print(num3 // num4, "- division without remainder")
                print(num3 % num4, "- the remainder after division")
                print(strin * 10,)
                break
            elif YourNom == "9":
                letters = "abcdefghijklmnopqrstuvwxyz"
                first_letter = letters[0]
                last_letter = letters[-1]
                print(first_letter, "- first letter")
                print(last_letter, "- last letter")
                break
            elif YourNom == "10":
                while True:
                    try:
                        side_a1 = int(input("Enter the first side: "))
                        side_a2 = int(input("Enter the second side: "))
                        side_a3 = int(input("Enter the third side: "))
                        if side_a1 + side_a2 > side_a3 and side_a1 + side_a3 > side_a2 and side_a3 + side_a2 > side_a1:
                            print(area(), "- area of a triangle")
                        else:
                            print("There is no such triangle")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                break
        else: print("Must contain a digit from 1 to 10")
    while True:
        rest = input("Press 1 to exit or 2 to restart: ")
        if rest == "1":
            ex = False
            break
        elif rest == "2":
            ex = True
            break
        elif rest != "1" and rest != "2":
            print("Enter 1 or 2!")
