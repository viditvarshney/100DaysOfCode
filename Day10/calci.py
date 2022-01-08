from logo import logo


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


symbols = ['+', '-', '/', '*']
operations = {'+': add, '-': subtract,
              '*': multiply, '/': divide}


def Calci():
    print(logo)
    num1 = float(input("Enter 1st number: "))
    for key in operations:
        print(key)

    while True:
        choice = input("Choose an operation: ")
        if not choice in symbols:
            print("WARNING! Invalid Operation symbol: ")
            break
        num2 = float(input("Enter next number: "))

        calculation_func = operations[choice]
        result = calculation_func(num1, num2)
        print(f"{num1} {choice} {num2} = {result}")
        clear = input(
            f"Type 'y to continue with {result} or 'new' to start a new calculation  'n' to exit: ")

        if clear.casefold() == 'y':
            num1 = result
        elif clear.casefold() == 'new':
            Calci()
        else:
            print(f"Your final result is: {result}")
            break


Calci()
