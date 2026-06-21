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