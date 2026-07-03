# Hashing is one way scrambling data to make it unreadable. It is a one-way function, meaning that once data is hashed, it cannot be easily reversed back to its original form. Hashing is commonly used for storing passwords securely, verifying data integrity, and creating unique identifiers for data.

import hashlib # builtin

# Hashing same input gives same output

password = "sizmoslothisawesome"

hashed = hashlib.sha256(password.encode()).hexdigest()
#.encode -> it concerts the string into bytes which is used by hashing functions
#sha256 -> a hashing algo produces a 256-bit hash value
#.hexdigest() -> returns the hash value as a hexadecimal string

print(f"Password: {password}")
print(f"Hashed: {hashed}")

#Password: sizmoslothisawesome
#Hashed: 00b5d60a070467a27379d5625abf88b7115336a4a71ea4274dd8bc63250ea5d4

# run it again — same input, same hash, every single time
hashed_again = hashlib.sha256(password.encode()).hexdigest()
print(hashed_again)
print(hashed == hashed_again)   # True — always identical for the same input

# EVEN A TINY CHANGE = COMPLETELY DIFFERENT HASH

password2 = "sizmoslothisnotawesome!"
hashed2 = hashlib.sha256(password2.encode()).hexdigest()
print(f"Password: {password2}")
print(f"Hashed: {hashed2}")

name = "sizmosloth"
encode = name.encode()
print(f"Name: {name}")
print(f"Encoded: {encode}")

# the usecase of hashing ---

# imagine this hash was saved to disk when you FIRST set your master password
stored_hash = hashlib.sha256("thismymasterpassword".encode()).hexdigest()

# later, when the app starts, you type your password again
attempt = input("Enter master password: ")
attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

if attempt_hash == stored_hash:
    print("Access granted!")
else:
    print("Wrong password!")

    