# Python Operators
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 ** 5)
print(10 // 5)
print(10 % 5)


# Python Assignment Operators
x = 5
print(x)

x += 3
print(x)
# now x is 8
x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)

x %= 3
print(x)

x //= 3
print(x)

x **= 3
print(x)

# x &= 3
# print(x)

# x |= 3
# print(x)

# x ^= 3
# print(x)

# x >>= 3
# print(x)

# x <<= 3
# print(x)

print(x := 3)


# Python Comparison Operators
x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x < y)

x = 5
y = 3
print(x >= y)

x = 5
y = 3
print(x <= y)

x = 5
y = 3
print(x > y)


# Python Logical Operators
x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 10)

x = 5
print(not(x > 3 and x < 10))


# Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is not y)
print(x != y)


# Python Membership Operators
x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("banana" not in x)


# Python Bitwise Operators
print(6 & 2)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3<<2)
print(3>>2)


# Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(100 + ~3)
print(8 >> 4 - 2)
print(6 & 2 + 1)
print(6 ^ 2 + 1)
print(6 | 2 + 1)
print(5 == 4 + 1)
print(not 5 == 4 + 1)
print(1 or 2 and 3)
print(4 or 5 + 10 or 8)
print(5 + 4 - 7 + 3)