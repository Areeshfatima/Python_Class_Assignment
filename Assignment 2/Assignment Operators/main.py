# Assignment Operators
# Assignment operators are used to assign values to variables:


# Using "=" 

a: int = 9
print("a =", a)

# Using "+="

b: int = 6
b += 3
print("b += 3 =", b )   # 9

# Using "-="

c: int = 5
c -= 3
print("c -= 3 =", c)    # 2

# Using "*="

d: int = 8
d *= 3
print("d *= 3 =", d)   # 24

# Using "/="

e: int = 9
e /= 3
print("e /= 3 =", e)   # 3.0

# Using "%="

f: int = 7
f %= 2
print("f %= 2 =", f)    # 1

# Using "//="

g: int = 12
g //= 5
print("g //= 5 =", g)   # 2

# Using "**="

h: int = 4
h **= 2
print("h **= 2 =", h)   # 16

# Using "&="

i: int = 9
i &= 2

# 9 = 1001
# 2 =   10
# becomes
# 0 = 0000

print("i &= 2 =", i)   # 0

# Using "|="

j: int = 9
j |= 2

# 9 = 1001
# 2 =   10
# becomes
# 11 = 1011

print("j |= 2 =", j)    # 11

# Using "^="

k: int = 9
k ^= 2

# 9 = 1001
# 2 =   10
# becomes
# 11 = 1011  

print("k ^= 2 =", k)   # 11

# Using ">>="

l: int = 9
l >>= 2


# 9 = 1001
# becomes (two shift)
#  2 = 10

print("l >>= 2 =", l)    # 2


# Using "<<="

m: int = 9
m <<= 2


# 9 = 1001
# becomes 
# 36 = 100100

print("m <<= 2 =", m)    # 36


# Using ":=" (walrus operator)

n: int = 9
print("n := 9 =", (n := 9))   # 9







