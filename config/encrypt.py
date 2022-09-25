from cryptography.fernet import Fernet

# Encryption Script
# Use one of the methods to get a key ( it must be the same when decrypting ) =
key = Fernet.generate_key()
input_file = 'config/config.json'
output_file = 'config/encrypted'
key_file = 'config/key.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

with open(key_file, 'w') as k:
    k.write(key.decode('utf-8'))

print(key.decode('utf-8'), "encrypt.py")
