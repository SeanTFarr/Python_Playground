# Calculator

#add art
from calc_art import logo
import os

#add function
def add(n1, n2):
    return n1 + n2

#subtract function
def subtract(n1, n2):
    return n1 - n2

#multiply function
def multiply(n1, n2):
    return n1 * n2

#divide function
def divide(n1, n2):
    return n1 / n2

# dictionary to store the operands as keys and the function names as values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# create calculator function
def calculator():
    print(logo)
    # Variable to ask for first number
    num1 = float(input("What is the first number?:"))

    #for loop to get operand
    for i in operations:
        print(i)

    should_continue = True

    while should_continue:
        # variable to ask what the operator is
        operation_symbol = input("Pick an operation: ")
        # Variable to ask for second number
        num2 = float(input("What is the next number?:"))
        # pick out the operator base on selection
        calculation_function = operations[operation_symbol]
        #create answer
        answer = calculation_function(num1, num2)
        # prinnt result
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        # check to see if user wants to continue
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()