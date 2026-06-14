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

#*ARGS MULTIPLE INPUTS LIKE IN SIDE A TUPLE FOR A FUNCTION---
def makepizza(size, *toppings):
    print(f"Make a {size} Pizza with toppings:")
    for topping in toppings:
        print(f"- {topping}")
makepizza("medium", "cheese", "mushrooms", "corn")

#**KWARGS LIKE MULTIPLE INPUTS BUT LIKE KEY AND VALUE PAIRS FOR A FUNCTION---
##IT TAKES KEYWORD ARGUMENTS---
def orderpizza(size, *toppings, **details):
    print(f"Make a {size} Pizza with toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print(details)         #as a dict
orderpizza("medium", "cheese", "mushrooms", "corn", payment = "COD", tip = "$5")

def orderpizza(size, *toppings, **details):
    print(f"Make a {size} Pizza with toppings:")
    for topping in toppings:
        print(f"- {topping}")
    for key, value in details.items():
        print(f"- {key} : {value}")
orderpizza("medium", "cheese", "mushrooms", "corn", payment = "COD", tip = "$5")


#USING FUNCTION TO CHANGE GLOBAL VARIABLE---
var = 100 #Global var
def change():
    x = 50 # Local var
    print(x)
change()

def change_global():
    global x
    x = 50
change_global()
print(x)

#FUNCTIONS ARE TREATED AS OBJECTS IN PY---
def sq(x):
    return x ** 2

def square(fun, num): # function as a argument
    return fun(num)

print(square(sq, 5))