fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

print(fruits[0]) 
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])
print(fruits[1:4])
print(fruits[:4])
print(fruits[2:])
print(fruits[:])

fruits.append("papaya")
fruits.insert(1, "grape")
fruits.remove("banana")
popped = fruits.pop()
print(popped)
print(fruits)

numbers = [1, 5, 2, 8, 7, 5, 3, 4, 6]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(numbers.count(3))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

for fruit in fruits:
    print(fruit)
