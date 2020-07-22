#print("hello")

while True:
    print("Press 1 Addition, 2 Substraction, 3 Multiplication, 4 Division, 5 Modulo, 6 Square, 7 Floor Division, 8 Exit:")

    choice = int(input("\nPlease enter your choice\n"))
    if choice == 1:
        number1 = int(input("Please Enter First number"))
        number2 = int(input("Please Enter First number"))
        print("\nAddition of", number1, "and", number2, "is", number1+number2)
    elif choice == 2:
        number1 = int(input("\nPlease Enter First number\n"))
        number2 = int(input("\nPlease Enter First number\n"))
        print("\nSubstraction of", number1, "and", number2, "is", number1 - number2)
    elif choice == 3:
        number1 = int(input("\nPlease Enter First number\n"))
        number2 = int(input("\nPlease Enter First number\n"))
        print("\nMultiplication of", number1, "and", number2, "is", number1 * number2)
    elif choice == 4:
        number1 = int(input("\nPlease Enter First number\n"))
        number2 = int(input("\nPlease Enter First number\n"))
        print("\nDivision of", number1, "and", number2, "is", number1 / number2)
    elif choice == 5:
        number1 = int(input("\nPlease Enter First number\n"))
        number2 = int(input("\nPlease Enter First number\n"))
        print("\nReminder of", number1, "and", number2, "is", number1 % number2)
    elif choice == 6:
        number1 = int(input("\nPlease Enter First number\n"))
        number2 = int(input("\nPlease Enter First number\n"))
        print("\nSquare of", number1, "and", number2, "is", number1 ** number2)
    elif choice == 7:
        number1 = int(input("\nPlease Enter First number\n"))
        number2 = int(input("\nPlease Enter First number\n"))
        print("\nFloor Division of", number1, "and", number2, "is", number1 // number2)
    elif choice == 8:
        break
    else:
        print("Please enter valid input")


