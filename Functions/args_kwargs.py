# ARGS AND KWARGS in py ---

# *args — positional, becomes a tuple
def total(*args):
    print(type(args))    # <class 'tuple'>
    return sum(args)
print(total(1, 2, 3, 4, 5))

# **kwargs — keyword, becomes a dict
def profile(**kwargs):
    print(type(kwargs))    # <class 'dict'>
    for k, v in kwargs.items():
        print(f"{k} = {v}")

profile(name="Samay", age=18, city="Ludhiana")

def combined(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

combined(1, 2, 3, 4, 5, name="Samay", age=18)

nums = [1, 2, 3]
print(*nums)

info = {"name": "Samay", "age": 18}
profile(**info)