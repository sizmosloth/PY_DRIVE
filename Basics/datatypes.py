x = 100
pi = 3.14159
name = "Samay Bagga"
is_pro = True
data = None
print(f"Integer: {x} (Type: {type(x)})")
print(f"Float: {pi} (Type: {type(pi)})")
print(f"String: '{name}' (Type: {type(name)})")
print(f"Boolean: {is_pro} (Type: {type(is_pro)})")
print(f"None: {data} (Type: {type(data)})")

#NUMERIC OPERATIONS
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(10 ** 2)

#BOOLEAN LOGIC
print(5 > 3)
print(5 < 3)
print(5 == 5)
print(5 != 3)
print(5 >= 5)
print(5 <= 3)
print(True and False)
print(True or False)
print(not True)

#BITWISE OPERATIONS
print(5 & 3)  # Bitwise AND
print(5 | 3)  # Bitwise OR
print(5 ^ 3)  # Bitwise XOR
print(~5)     # Bitwise NOT
print(5 << 1) # Left shift
print(5 >> 1) # Right shift

#BOOLEAN AS NUMBER
print(True + 1)   # True is treated as 1
print(False + 1)  # False is treated as 0
print(True + True)  # True + True = 2