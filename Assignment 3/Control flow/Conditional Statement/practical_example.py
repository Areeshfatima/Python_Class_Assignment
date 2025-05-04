# Simple Calculator
operation: str = input("Enter the Operation you want to perform (+, -, *, /, **, %): ")
num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num1 >= num2:
        result = num1 / num2
    else:
        result = "Error: Make sure your num1 is greater than num2."
elif operation == "**":
    result = num1 ** num2
elif operation == "%":
    result = num1 % num2
else:
    result = "Invalid Operation"

print("Result: ", result)
    