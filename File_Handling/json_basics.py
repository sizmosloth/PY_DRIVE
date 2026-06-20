# JSON in Pyton
# JSON javascript Object Notation
# It's just a text format for storing data - looks excatly like py dicts or lists

# the problem json solves:
# you can only write STRINGS to a file with f.write()
# but your data is dicts, lists, numbers, booleans...
# json converts that data to text (to save it) and back (to load it)

import json

student = {
    "name" : "Samay",
    "age" : "18",
    "skills" : ["Python", "Git"],
    "is_pro" : True
}

# Converting into json string
json_string = json.dumps(student, indent = 4)
print(json_string)
print(type(json_string))

# Saving to a file
with open("students.json", "w") as f:
    json.dump(student, f, indent = 4)

# Load from a file
with open("students.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data)
print(type(loaded_data))
print(loaded_data["name"])

# JSON string to py object
raw_text = '{"name": "Samay", "age": 18}'
parsed = json.loads(raw_text)
print(parsed)
print(type(parsed))    # <class 'dict'>