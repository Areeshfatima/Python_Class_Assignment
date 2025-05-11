# Problem Practice
# Write a Python program that asks the user for two numbers and divides them.
# Use exception handling to catch any errors that might occur (e.g., division by zero or invalid input).

try:
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter a number:"))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot didvided by zero.")
except ValueError:
    print("error: Invalid input, Enter a number.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you! For using it.")



