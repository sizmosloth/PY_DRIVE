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

