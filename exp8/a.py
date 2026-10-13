from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b"8BYTEKEY"
message = "Hello DES Algorithm!"

cipher = DES.new(key, DES.MODE_CBC)
encrypted = cipher.encrypt(pad(message.encode(), 8))

decipher = DES.new(key, DES.MODE_CBC, iv=cipher.iv)
decrypted = unpad(decipher.decrypt(encrypted), 8).decode()

print("Original:", message)
print("Encrypted:", encrypted.hex())
print("Decrypted:", decrypted)
