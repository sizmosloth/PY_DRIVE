#FUNCTONS---

def greet():
    print("Hello, Greet Function")

greet() #call

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Samay") #call

def sum_num(a, b):
    print(f"The sum of {a} and {b} is: {a + b}")

sum_num(2, 3)

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(f"The product of 4 and 5 is: {result}")

#DEFAULT PARAMETERS---
def greet(name, message="Good Morning"):
    print(f"{message}, {name}!")

greet("Alice")  # Uses default message
greet("Bob", "Hello")  # Overrides default message

#RETURN VALUE---
def get_fullname(first, last):
    full_name = f"{first} {last}"
    return full_name
name = get_fullname("Samay", "Bagga")
print(name)

#RETURN MULTIPLE---
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

low, high, total = get_stats([3, 6, 5, 7, 8, 9])
print(low, high, total)
