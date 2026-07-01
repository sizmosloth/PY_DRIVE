# About Cryptography Fernet for Encryption and Decryption

from cryptography.fernet import Fernet

# generate a random encryption key
key = Fernet.generate_key()
print(key)   # this is bytes, looks like gibberish — that's normal

cipher = Fernet(key)

# encrypt something
secret = b"my super secret password"   # note the b" " — Fernet needs bytes, not a normal string
encrypted = cipher.encrypt(secret)
print(encrypted)

# decrypt it back
decrypted = cipher.decrypt(encrypted)
print(decrypted)   # back to the original
print(decrypted.decode())   # .decode() turns bytes back into a normal readable string