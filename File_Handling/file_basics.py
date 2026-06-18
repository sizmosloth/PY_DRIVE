# FILE HANDLING IN PYTHON ---

# this is how python reads/write actual files on disk

# WRITING TO A FILE ---

with open("notes.txt", "w") as f:
    f.write("Hello now these are my Python notes. \n")
    f.write("PYTHOOOOOONNNNNNNNNNNNNNNNNNNNN\n")

# "w" -> write , "notes.txt" is created if exists its get overwritten

# READING A FILE ---

with open("notes.txt", "r") as f:
    content = f.read()
print(content)

# "r" -> read , .read() -> grabs the entire file

# FOR READING LINE BY LINE ---

with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip()) # .strip() removes the extra \n at the end 

# APPENDING --- adding without erasing 

with open("notes.txt", "a") as f:
    f.write("PYTHONSNUHDUB\n")

# "a" -> append mode 


# LEARNED ->
# used with because it closes the file when done without it need to use f.close() and if forget then memory leak

f = open("notes.txt", "r")
content = f.read()
f.close()