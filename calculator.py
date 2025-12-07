print("Welcome to the Calculator!")
print("Here are the available operations: '+', '-', '*', '/' '%', '^' (exponentiation), 'sqrt' (square root)")
while True:
    a=int(input("enter the first number(a):"))
    b=int(input("enter the second number(b):"))
    oper = input("Enter the operation you want to perform: ")

    if oper in [ '+', 'add', 'addition', 'plus', 'sum' ]:
        print("The sum of the two numbers is:", a+b)

    elif oper in [ '-', 'subtract', 'subtraction', 'minus', 'difference' ]:
        print("The difference of the two numbers is:", a-b)

    elif oper in [ '*', 'multiply', 'multiplication', 'product', 'times' ]:
        print("The product of the two numbers is:", a*b)

    elif oper in [ '/', 'divide', 'division', 'quotient' ]:
        if b != 0:
            print("The quotient of the two numbers is:", a/b)
        else:
            print("Error: Division by zero is not allowed.")
    elif oper in [ '%', 'modulus', 'mod' ]:
        if b != 0:
            print("The modulus of the two numbers is:", a%b)
        else:
            print("Error: Modulus by zero is not allowed.")
    elif oper in [ '^', 'exponent', 'power' ]:
        print("The result of exponentiation is:", a**b)
    elif oper in [ 'sqrt', 'square root' ]:
        if a >= 0:
            import math
            print("The square root of the first number is:", math.sqrt(a))
        elif a<0:
            import cmath
            print("The square root of the first number is:", cmath.sqrt(a))
        else:
            print("Error: Cannot compute square root of a negative number.")
    elif oper in [ 'exit', 'quit', ]:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid operation. Please try again.")