print("Welcome to the Calculator!")
print("Here are the available operations: '+', '-', '*', '/' '%', '^', 'sqrt', 'ordinal'")

while True:
    oper = input("Enter the operation you want to perform: ")
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))

    if oper in ['+', 'add', 'addition', 'plus', 'sum']:
        print("The sum of the two numbers is:", a + b)
        print("")

    elif oper in ['-', 'subtract', 'subtraction', 'minus', 'difference']:
        print("The difference of the two numbers is:", a - b)
        print("")

    elif oper in ['*', 'multiply', 'multiplication', 'product', 'times']:
        print("The product of the two numbers is:", a * b)
        print("")

    elif oper in ['/', 'divide', 'division', 'quotient']:
        if b != 0:
            print("The quotient of the two numbers is:", a / b)
            print("")
        else:
            print("Error: Division by zero is not allowed.")
            print("")

    elif oper in ['%', 'modulus', 'mod']:
        if b != 0:
            print("The modulus of the two numbers is:", a % b)
            print("")
        else:
            print("Error: Modulus by zero is not allowed.")
            print("")

    elif oper in ['^', 'exponent', 'power', '**']:
        print("The result of exponentiation is:", a ** b)
        print("")

    elif oper in ['sqrt', 'square root']:
        import math, cmath
        if a >= 0:
            print("The square root of the first number is:", math.sqrt(a))
            print("")
        else:
            print("The square root of the first number is:", cmath.sqrt(a))
            print("")
    elif oper in ['ordinal', 'ord']:
        def get_ordinal(n):
            if 10 <= n % 100 <= 20:
                suffix = 'th'
            else:
                suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
            return str(n) + suffix
        
        print(f"The ordinal form of {a} is: {get_ordinal(a)}")
        print("")
    elif oper in ['exit', 'quit']:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid operation. Please try again.")
        print("")