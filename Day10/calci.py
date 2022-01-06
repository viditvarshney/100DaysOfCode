
num1 = float(input("Enter 1st number: "))


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


operations = {'+': add, '-': subtract,
              '*': multiply, '/': divide}

for key in operations:
    print(key)

while True:
    choice = input("Choose an operation: ")
    num2 = float(input("Enter next number: "))

    calculation_func = operations[choice]
    result = calculation_func(num1, num2)

    print(f"{num1} {choice} {num2} = {result}")
    if input(f"Type 'y to continue with 9.0 or 'n' to exit: ").casefold() == 'y':
        num1 = result
    else:
        print(f"Your final result is: {result}")
        break
