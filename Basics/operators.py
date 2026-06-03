#ARITHMETIC

print(10 + 2)  #12
print(10 - 2)  #8
print(10 * 2)  #20
print(10 / 2)  #5.0
print(10 // 3) #3 (floor division)
print(10 % 3)  #1 (modulo)
print(10 ** 2) #100 (exponentiation)

#COMPARISON
x = 10
y = 20
print(x > y)   #False
print(x < y)   #True
print(x == y)  #False
print(x != y)  #True
print(x >= y)  #False
print(x <= y)  #True

#LOGICAL
age = 18
id = True
print(age >= 18 and id)  #True
print(age >= 18 or id)   #True
print(not id)            #False

#ASSIGNMENT
x = 10
x += 5  # x = x + 5 -> 15
x -= 3  # x = x - 3 -> 12
x *= 2  # x = x * 2 -> 24
x /= 4  # x = x / 4 -> 6.0
x //= 2 # x = x // 2 -> 3.0
x %= 2  # x = x % 2 -> 1.0
x **= 3 # x = x ** 3 -> 1.0

name = "Samay"
name += " Bagga"  # name = name + " Bagga" -> "Samay Bagga"
print(name)

fruit = ["apple", "banana", "orange"]
print("apple" in fruit)  #True
print("grape" in fruit) #False
print(name is "Samay Bagga")  #True (same string literal)
