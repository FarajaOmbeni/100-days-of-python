import os
import art
clear = lambda: os.system('clear')

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](3,2))

start_over = False
continue_with_answer = True

while not start_over:
    print(art.logo)
    n1 = float(input("What's the first number? "))
    while continue_with_answer:
        for operation in operations:
            print(operation)
        picked_operation = input("Pick an operation: ")
        n2 = float(input("What is the next number? "))
        for operation in operations:
            if(picked_operation == operation):
                answer = operations[picked_operation](n1,n2)
                print(f"{n1} {picked_operation} {n2} = {answer}")
        ask = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")
        if(ask == 'y'):
            n1 = answer
        else:
            continue_with_answer = False
            clear()
