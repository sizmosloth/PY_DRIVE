person = {
    "name" : "Samay",
    "age" : 18,
    "city" : "Ludhiana"
}

print(person)
print(person["name"])
print(person["age"])
print(person["city"])   
person["age"] = 19
print(person["age"])
person["country"] = "India"
print(person)
person.pop("country")

student = {
    "name": "Samay",
    "marks": 95,
    "grade": "A"
}
for key in student:
    print(key, ":", student[key])
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

users = {
    "user1": {"name": "Samay", "age": 20},
    "user2": {"name": "Rahul", "age": 22}
}

print(users["user1"]["name"])
print(users["user2"]["name"])