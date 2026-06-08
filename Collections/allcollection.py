#PYTHON COLLECTION OVERVIEW OF ALL DATA STRUCTURES
#LISTS
#TUPLES
#SETS
#DICTIONARIES

#-------------------------------------------------




#list---------------------------
fruits = ["apple", "banana", "cherry", "Litchi"]
print(fruits)
print(fruits[0])
print(fruits[1:3])

fruits.append("orange")
fruits.insert(1, "grape")
fruits.remove("apple")

numbers = [5, 4, 3, 2, 1]
numbers.sort()
print(numbers)
print(len(numbers))
print(3 in numbers)
print(numbers.count(3))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

double = [x * 2 for x in numbers]
odd = [x for x in numbers if x % 2 != 0]
print(double)
print(odd)





#TUPLES--------------------
coordinates = (10, 20)
person = ("Samay", 18, "Ludhiana")
print(coordinates[0])
print(person[1])

name , age , city = person
print(name)
print(age)
print(city)





#DICTIONARIES--------------------
students = {
    "Samay": {"age": 18, "city": "Ludhiana"},
    "Pihu": {"age": 18, "city": "Danapur"},
    "Rajveer": {"age": 19, "city": "Amritsar"}
}
print(students["Samay"])
print(students["Pihu"]["city"])
print(students.get("Rajveer"))

for name, info in students.items():
    print(f"{name} is {info['age']} years old and lives in {info['city']}.")

print(students.keys())
print(students.values())





#SETS--------------------

fruits = {"apple", "banana", "cherry", "Litchi"}
print(fruits)
nums = {5, 4, 4, 4, 3, 2, 1}
new_num = set(nums)
print(new_num)

a = {5, 6, 7, 8}
b = {7, 8, 9, 10}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)