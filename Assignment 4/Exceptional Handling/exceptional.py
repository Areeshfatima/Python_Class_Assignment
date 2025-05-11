# Exception Handling with try, except, else, and finally
# Exception handling is a crucial part of writing robust Python programs. It allows you to handle errors gracefully and ensure your program doesn't crash unexpectedly.


# 1. The try Block
# The try block is used to test a block of code for errors. 
# If an error occurs within the try block, the program will immediately jump to the except block (if provided).

try:
    result = 10 / 0     # This will raise a ZeroDivisionError
except:
    print("An error occured!")


# The except Block
# The except block is used to handle specific errors that occur in the try block.
# You can specify the type of error to catch, or use a generic except to catch all errors.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can not divided by zero!")
except Exception as e:
    print(f"An unexpexcted error occured: {e}")


# The else Block
# The else block is executed if no errors occur in the try block. 
# It is optional and is used for code that should only run when the try block is successful.

try:
    result = 10 / 5
except ZeroDivisionError:
    print("cannot divided by zero!")
else:
    print(f"Division Successful:Result = {result}")

# The finally Block
# The finally block is executed regardless of whether an error occurred or not. 
# It is often used for cleanup operations, such as closing files or releasing resources.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can not divided by zero!")
finally:
    print("This will always excecute!")

print("\n----\n")

# 5. Putting It All Together

def divided_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
    except ZeroDivisionError:
        print("Error: Cannot divided by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required!")
    else:
        print(f"Division successfull. Result: {result}")
    finally:
        print("Operation successfully!")

divided_numbers(10, 20)  # Division successfull
divided_numbers(5, 0)    # ZeroDivisionError
divided_numbers(12, "8")  # TypeError

# Play with Exception Handling in order to understand

def divided_numbers(x, y):
    try:
        result = x / y
    # except Exception as e:
    #     print(f"Exception: An unexcepted error occured: {e}")
    except ZeroDivisionError:
        print("ZeroDivisionError: can not divided by zero!")
    except TypeError:
        print("TypeError: Invalid input type, Number required!")
    # except Exception as e:
    #     print(f"Exception: An unexcepted error occured: {e}")
    else:
        print(f"else: division Successfull! Result = {result}")
    finally:
        print("finally: Operation Complete! \n")

divided_numbers(8, 4)
divided_numbers(10, 0)
divided_numbers(56, "78")

# Learning code on error handling covering all the excepts

import random
from typing import Tuple, List, Dict

def generate_random_data(num_samples: int) -> List[Tuple[int, int]]:
    # Generates a list of random number pairs.
    try:
        if not isinstance(num_samples, int) or num_samples <= 0:
            raise ValueError("numbers of sample must be positive integers.")
        data = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_samples)]
        return data
    except ValueError as ve:
        print(f"Error: {ve}")
        return []  # Return empty list on error
    except Exception as e:
        print(f"An Unexcepted Error occured: {e}")
        return []
    
def calculate_ratios(data: List[Tuple[int, int]]) -> List[float]:
    """Calculates the ratio of the first number to the second in each pair."""
    ratios = []
    try:
        for pair in data:
            num1, num2 = pair
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            if not isinstance(num1, int) or not isinstance(num2, int):
                raise TypeError("Input data must be integers")
            ratio = round(num1 / num2, 2)
            ratios.append(ratio)
        return ratios 
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        return []
    except TypeError as te:
        print(f"Error: {te}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during ratio calculation: {e}")
        return []

def process_data(num_samples: int) -> List[float]:
    """Combines data generation and ratio calculation with comprehensive error handling."""
    data = generate_random_data(num_samples)
    if not data:      # check if generate_random_data returns an empty list which means it had an error
        return []
    ratios = calculate_ratios(data)
    return ratios

# ratios = process_data(5)
# print(f"Calculated Data: {ratios}")

# Example usage with error handling

try:
    num_samples = 10
    result = process_data(num_samples)

    if result:
        print("calculated ratios:", result)
    else: # if process_data returned an empty list it means there was some error
        print("Data processing failed due to an error.")
except Exception as e:   # catching unexpected errors
    print(f"An unexcepted error occured: {e}")

# example of invalid input
result = process_data(-2)
if not result:
    print("Numbers must be in positive integers, data processing failed.")

result = process_data("abc")
if not result:
    print("Invalid input type, data processing failed")

# How a Function Throws an Exception in Python?
def divided(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed!")   # Raising an exception
    return a / b
print(divided(12, 6))
# print(divided(30, 0))

# Handling the Exception with try-except
def divide(x, y):
    if y == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return x / y

try:
    result = divide(4, 0) # This will raise an exception
    print(result)  # This line won't run if exception occurs
except ValueError as ve:
    print(f"Error: {ve}")

print("Program continue...")     # This line will always execute

# Throwing Custom Exceptions

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative integers are not allowed!")
    return f"{n} is positive"
try:
    print(check_positive(-7))   # Raise NegativeNumberError
except NegativeNumberError as nne:
    print(f"Custom Exception Caught: {nne}", "-Exception Class Type:", type(nne))

# What is NoReturn?
# NoReturn is a special type hint from Python's typing module. It is used to indicate that a function will not return normally. This means the function either:
# Always raises an exception,
# Enters an infinite loop,
# Or otherwise never reaches the end of the function body to return a value.

# Example: Using NoReturn

from typing import NoReturn

def terminate_program() -> NoReturn:
    """Terminate the program by raising an exception."""
    raise SystemExit("Terminating the Program..")

# When you call terminate_program, it never returns normally:
try:
    terminate_program()
except SystemExit as se:
    print(f"Program terminated: {se}")

# Alternative to NoReturn in Python
# NoReturn from the typing module is used to indicate that a function never returns normally. 
# However, if you don’t want to use NoReturn, you have a few alternative approaches.

# Example: Using None
def log_error(message: str) -> None:
    """Logs an error message but does not terminate the program."""
    print(f"Error: {message}")
log_error("Something went wrong!")

# Alternative: Omitting the Return Type Hint

def terminate_program():
    """Terminates the program by raising an exception."""
    raise SystemExit("Program is terminating..")

terminate_program()








    

    

    



    




    
         

                 








