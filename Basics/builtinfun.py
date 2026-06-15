# PYTHON built in functions

# Basic functions ---
print(len([1, 2, 3]))        # 3   — length
print(type("hello"))         # str — type of value
print(int("18"))             # 18  — convert to int
print(str(100))              # 100 — convert to string
print(float("3.14"))         # 3.14
print(input("enter: "))      # takes user input

# Maths functions ---
print(max(3, 7, 1))          # 7   — biggest value
print(min(3, 7, 1))          # 1   — smallest value
print(sum([1, 2, 3, 4]))     # 10  — adds everything
print(abs(-50))              # 50  — removes negative
print(round(3.7))            # 4   — rounds off
print(pow(2, 10))            # 1024 — 2 to the power 10

# List functions ---
print(list("hello"))         # ['h','e','l','l','o']
print(tuple([1, 2, 3]))      # (1, 2, 3)
print(set([1, 1, 2, 3]))     # {1, 2, 3} — removes duplicates
print(range(5))              # range(0, 5)
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list(range(1, 6)))     # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8] — step

# Sorted function --- returns a sorted list
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sorted(nums))
print(sorted(nums, reverse = False))

words = ["Samay", "Bagga", "Is", "A", "Goat"]
print(sorted(words))         # alphabetical

print(sorted(words, key = len)) # key = sort by what?

# Map --- Is a function to every item
num = [1, 2, 3, 4, 5]

result = []   # without map
for n in num :
    result.append(n ** 2)
print(result)

result = list(map(lambda x : x ** 2 , nums))   # with map
print(result)

def double(x):   # map with normal function
    return x * 2

result = list(map(double, nums))
print(result)  