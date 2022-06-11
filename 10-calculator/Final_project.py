from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract, 
    "*" : multiplication,
    "/" : division
}

def calculator():
    num1 = float(input("Enter first number: "))

    for key in operations:
        print(key)

    choice = True
    while choice:
        operation_symbol = input("Pick a symbol given above to proceed. ")
        num2 = float(input("Enter second number: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit").lower() == 'y':
            num1 = result
        else:
            choice = False
            calculator()

print(logo)
calculator()