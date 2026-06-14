# LAMBDA fuction one line anonymous function ---

# NORMAL

def square( num ):
    return num ** 2

# LAMBDA

square = lambda x : x ** 2
print(square(5))
print((lambda x : x ** 2)(5))

add = lambda a, b, c : a + b + c
print(add(3, 2, 1))

def my_fun(fun , arr):
    result = []
    for items in arr:
        newitems = fun(items)
        result.append(newitems)
    return result

nums = [1, 2, 3, 4, 5]

square = my_fun(lambda x : x ** 2, nums)

print(square)