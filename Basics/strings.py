name = "Samay"
city = "Ludhiana"

print("Name:", name)
print("City:", city)

print("Length of name:", len(name))
print("Length of city:", len(city))
print("Uppercase name:", name.upper())
print("Lowercase city:", city.lower())
print("Is name alphabetic?", name.isalpha())
print("Is city alphabetic?", city.isalpha())
print("Does name start with 'S'?", name.startswith('S'))
print("Does city end with 'a'?", city.endswith('a'))
print(name[0])
print(city[1:5])
print(name + " from " + city)

age = 18
print(f"My name is {name} and I am {age} years old.")
print(f"I live in {city.upper()}.")

email = "samaybagga8@gmail.com"
print("Email:", email)
print("Username:", email.split('@')[0])
print("Domain:", email.split('@')[1])
print(email.startswith("samay"))
print(email.endswith(".com"))
print("gmail" in email)

bio = """
Name : Samay Bagga
Age : 18
City : Ludhiana
Occupation : Student
"""
print(bio)