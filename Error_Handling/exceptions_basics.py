# Error handling in python (a.k.a EXCEPTIONS)

# errors in python are called "exceptions"
# when something goes wrong, python "raises" an exception
# if you don't handle it, your whole program CRASHES

# ---
# WHAT A CRASH LOOKS LIKE — try this WITHOUT try/except first
# ---
# age = int("samay")
# this line would crash your entire program with:
# ValueError: invalid literal for int() with base 10: 'samay'

# Basic TRY/EXCEPT

try :
    age = int("samay")
    print(age)
except:
    print("Something went wrong!")
# program keeps running instead of crashing — this is the whole point

# Catching the specific error

try:
    age = int("samay")
except ValueError:
    print("That's not a valid number!")   

# COMMON BUILT-IN EXCEPTIONS YOU'LL ACTUALLY SEE

# ValueError — wrong type of value
try:
    num = int("hello")
except ValueError:
    print("ValueError: couldn't convert that to a number")

# ZeroDivisionError — dividing by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: can't divide by zero")

# IndexError — accessing a list index that doesn't exist
try:
    fruits = ["apple", "mango"]
    print(fruits[5])
except IndexError:
    print("IndexError: that index doesn't exist")

# KeyError — accessing a dict key that doesn't exist
try:
    student = {"name": "Samay"}
    print(student["age"])
except KeyError:
    print("KeyError: that key doesn't exist")

# TypeError — wrong type used in an operation
try:
    result = "5" + 5
except TypeError:
    print("TypeError: can't add a string and an int")

# FileNotFoundError — you already saw this one in File_Handling
try:
    with open("doesnt_exist.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("FileNotFoundError: that file doesn't exist")

# CATCHING MULTIPLE DIFFERENT ERRORS ---

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)
except ValueError:
    print("That wasn't a valid number")
except ZeroDivisionError:
    print("Can't divide by zero")

# GETTING THE ACTUAL ERROR MESSAGE ---

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    # "as e" lets you grab the actual error object and print/use it

# ELSE — runs ONLY if no error happened
try:
    num = int("25")
except ValueError:
    print("Invalid number")
else:
    print(f"Success! You entered {num}")

# FINALLY — ALWAYS runs, error or not
try:
    num = int("samay")
except ValueError:
    print("Invalid number")
finally:
    print("This always runs, no matter what")
# useful for cleanup — like closing a file or a connection, whether the code above succeeded or failed

# Raising own errors ---

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print(f"Transaction failed: {e}")

# "raise" lets YOU trigger an error on purpose, with your own message