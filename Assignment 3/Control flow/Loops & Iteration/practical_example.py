#  Sum of numbers

# sum of numbers from 1 to 150

total: int = 0

for i in range(1, 150):
    total += 1
print("Sum of numbers from 1 to 150 is:", total)


# Finding factors of a numbers

num: int = 69
factors = []

for i in range(1, num + 1):
    if num % 1 == 0:
        factors.append(i)
    print(f"Factors of {num} : {factors}")