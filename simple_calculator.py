


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b 
def divide(a, b):
    return a / b


user_input = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
if user_input in ('add', 'subtract', 'multiply', 'divide'):
    num1 = float(input ("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if user_input == 'add':
        print (f"{num1} + {num2} = {add(num1, num2)}")
    elif user_input == 'subtract':
        print(f"{num1} - {num2} = {subtract(num1,num2)}")
    elif user_input == 'multiply':
        print(f"{num1} * {num2} = {multiply(num1,num2)}")
    elif user_input == 'divide':
        print(f"{num1} / {num2} = {divide(num1,num2)}")
else:
    print("Invalid operation. Please enter add, subtract, multiply, or divide.")


