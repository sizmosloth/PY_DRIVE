# Password Manager =)

import hashlib
import os

master_hash_file = "master.hash"

def masterpasssetup():
    if os.path.exists(master_hash_file):
        return
    
    print("No master password found. Please set up a new master password.")
    password = input("Enter a new master password: ")

    hashed = hashlib.sha256(password.encode()).hexdigest()

    with open(master_hash_file, "w") as f:
        f.write(hashed)
    print("Master password set up successfully.")

def verifympassword():
    with open(master_hash_file, "r") as f:
        stored_hash = f.read()

    attempt = input("Enter master password: ")
    attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

    return attempt_hash == stored_hash

# TESTING

masterpasssetup()

if verifympassword():
    print("Access granted! Vault unlocked.")
else:
    print("Wrong password. Access denied.")

# this creates a master password and stores it in a hashed format. It then verifies the password when the user tries to access the vault.