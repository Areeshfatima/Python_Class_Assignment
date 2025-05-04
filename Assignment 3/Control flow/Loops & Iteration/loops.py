# Loops and Iteration
# Loops are used to repeate a block of code multiple times.Python supports two types of loops.
# for loops: used to iterate over sequence (lists, ranges or strings)
# while loops: used to repeate a block of code as long as the condition is True

# The for loop

vegetables:list[str] = ["Potato", "Tomato", "Peas", "Carrot"]

for vegetable in vegetables:
    print(vegetable)


word: str = "Education"

for letters in word:
    print(letters)


# for loop with else(no break)

food_order: list[str] = ["Biryani", "Manchurian", "Rasmalia", "Chocolate Shake"]

for food in food_order:
    print(food)
else:
    print("Order received successfully!")


# for loop with else(with break)

ice_cream: list[str] = ["Vanila", "Chocolate", "Strawberry", "butterscotch"]

for flavors in ice_cream:
    print(flavors)
    if flavors == "Strawberry":
        print("Order cancel!")
        break
else:
    print("Order done successfully")    # This will not run


# Searching with else

multiple_of_6: list[int] = [6, 12, 18, 24, 30]

for num in multiple_of_6:
    if num == 36:
        print("Number found!")
        break
else:
    print("Number not found!")    # runs because 36 is not present

# foor loop with range

for i in range(9):
    print(i)


for i in range(3, 15, 2):     # start, end, steps
    print(i)

# "_" underscore throwaway varaible

for _ in range(9):   # it is a loop variable, but its throwaway variable
    print(f"Learning Python is interesting! Iteration { _ }")


#  The while loop

table_of_2: int = 2

while table_of_2 <= 20:
    print(table_of_2)
    table_of_2 += 2


# Controlling loop
# python provides two keywords(break & continue) to control loops.

# Break: Exits the loop immediately

for i in range(15):
    if i == 10:
        break
    print(i)

# Continue: Skips the rest of the code in the current iteration and moves to the next iteration.

for i in range(20):
    if i == 18:
        continue
    print(i)

# Nested loops

for outer in range(1, 6):  #outer loop
    print(f"Multipication table for {outer}: ")
    for inner in range(1, 6):   # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()    # add a blank line after each row









