# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:


# Decimal numbers and their binary values:
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
# 4 = 100
# 5 = 101
# 6 = 110
# 7 = 111
# 8 = 1000
# 9 = 1001
# 10 = 1010
# 11 = 1011
# 12 = 1100
# 13 = 1101
# 14 = 1110
# 15 = 1111
# 16 = 10000


x: int = 6    # 110
y: int = 3     # 11   
            

# AND 
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:


print("x & y =", x & y)  # 2

# OR
# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:


print("x | y =", x | y)  # 7


# XOR ^
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0


print("x ^ y =", x ^ y)     # 5


# Not ~


print("~x =", ~x )   # -7     Flips all bits and adds 1 (two's complement representation)



# Zero fill left shift
# The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:
	
# If you push 00 in from the left:
# 3 = 11         6 = 110
# becomes        becomes
# 12 =1100       16 = 11000

print("y << 2 =", y << 2)    # 12
print("x << 2 =", x << 2)    # 24


# Signed right shift
# The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

# If you move each bit 2 times to the right, 6 becomes 1 :
# 6 =110        3 = 11
# becomes       becomes
# 1 = 10        0 = 00

print("x >> 2 =", x >> 2)    # 1
print("y >> 2 =", y >> 2)    # 0
   