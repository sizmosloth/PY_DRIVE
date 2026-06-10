#FOR LOOPS-----
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for char in "Samay":
    print(char)

for i in range(5):
    print(i)
for i in range(2, 10, 2):
    print(i)




#WHILE LOOPS------
count = 0
while count < 5:
    print(count)
    count += 1

while True:
    name = input("Enter your name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    print(f"Hello, {name}!")




#BREAK AND CONTINUE------
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


for i in range (5):
    print(i)
else:
    print("Loop completed successfully.")



#NESTED LOOPS------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")