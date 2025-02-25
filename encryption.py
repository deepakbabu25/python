import string
import random
chars=" "+string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)

print(chars)


plainText=input("Enter the text you want to encrypt: ")
cipherText=""
for i in plainText:
    index = chars.index(i)
    cipherText+=key[index]
print("Encrypted text: ",cipherText)

# Decryption
cipherText=input("Enter the text you want to decrypt: ")
plainText=""
for i in cipherText:
    index = key.index(i)
    plainText+=chars[index]
print("decrypted text: ",plainText)