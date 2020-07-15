#control statments 2Assignment

number1 = int(input("Enter number1"))
number2 = int(input("Enter number2"))

if number1>number2:
    result = number1 - number2
    print(number1,"is greater","substraction is", result)
else:
    result = number2 - number1
    print(number2, "is greater", "substraction is",result)