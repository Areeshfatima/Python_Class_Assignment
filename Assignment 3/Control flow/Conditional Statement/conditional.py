# Conditional Statement
# Used to execute different blocks of code based on condition.

# if Statement
# The if statement is used to execute the block of code only if a condition is True.

summer_temperature: int = 40

if summer_temperature > 30:
    print("Heatwave Alert!")
    print("Stay Hydrated")


# else Statement
# The else statement is used to execute the block of code if the if condition is False.

winter_temperature: int = 15

if winter_temperature > 18:
    print("Today is very cold") 
    print("Stay Home and safe")
else:
    print("The weather is pleasant.!!")


# elif statement
# The elif statement is used to check multiple conditions.It stands for "else if"

age: int = 22

if age >= 18:
    print("Eligible, you can vote..")
elif age <= 18:
    print("NOt eligible, Sorry you can't vote yet!!")
else:
    print("Make sure you have your identity card for vote..!!") # if both conditions is Flase then it runs


# Ternary Operator
# we also write our if else statement ia a single line by using ternary operators.
traffic_signals: str = "red"

print("You can go") if traffic_signals == "green" else print("Stopped, wait!")

# Using Logical Operators with conditional Statement

# and

driving_age: int = 20
driving_license: bool = True

if driving_age >= 18 and driving_license:
    print("You are Eligible.")
else:
    print("Not eligible!")

# or

pay_bill_credit: bool = False
pay_bill_cash: bool = True

if pay_bill_credit or pay_bill_cash:
    print("Your electricity bill is paid..!!")

# not

student = False

if not student: 
    print("Work Hard.!!")
else: 
    print("Be a good student")

# nested if statement

shops_open: bool = True
bakery_shop: bool = False

if shops_open == True:    # if its True then check nested statement 

    if shops_open == bakery_shop:    # after the above condition is True then check nested statement is True 
        print("Buy Cakes and biscuits at this shop..!")    # if True this statement will run
    else:
        print("Buy any Refreshment items for guest at any shop..!!")  # if False then this statement will run

else:
    print("All Shops were closed today due to strike.!")   # if the 1st condition is False so this statement will run directly their is no need to check nested statement


