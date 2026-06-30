def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Choose (+, -, *, /): ")

if choice == "+":
    print("Result =", add(num1, num2))
elif choice == "-":
    print("Result =", subtract(num1, num2))
elif choice == "*":
    print("Result =", multiply(num1, num2))
elif choice == "/":
    print("Result =", divide(num1, num2))
else:
    print("Invalid choice")