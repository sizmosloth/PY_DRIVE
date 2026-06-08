fruits = {"apple", "banana", "cherry", "Litchi"}
print(fruits)

fruits.add("orange")
fruits.remove("banana")
print(fruits)

#to remove duplicates
numbers = [5, 5, 5, 4, 3, 2, 1]
numberset = set(numbers)
print(numberset)

#set operations 
a = {5, 6, 7, 8}
b = {7, 8, 9, 10}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

members = {"Samay", "Pihu", "Rajveer"}
user = "Samay"
if user in members:
    print(f"{user} is a member.")
else :
    print(f"{user} is not a member.")