coordinates = (13.3456, 45.6789)
colors = ("red", "green", "blue")
mixed_tuple = (18, "Samay", 3.14, True)

print(coordinates)
print(coordinates[0]) 
print(colors[1])
print(mixed_tuple[2])

lat, long = coordinates
print("Latitude:", lat)
print("Longitude:", long)

r , g , b = colors
print("Red:", r)
print("Green:", g)
print("Blue:", b)

students = {
    ("Samay" , 95),
    ("Amit" , 88),
    ("Riya" , 92)
}
for name , score in students:
    print(f"{name}: {score}")

nums = (1, 2, 3, 4, 2, 5, 6, 9)
print(nums.count(2))
print(nums.index(4))