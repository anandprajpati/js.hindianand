def encrypt(text, s):
    cipher_t = ""
    for char in text:
        if char.isupper():
            cipher_t += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            cipher_t += chr((ord(char) + s - 97) % 26 + 97)
        else:
            cipher_t += char  # leave non-alphabetic characters unchanged
    return cipher_t

def decrypt(cipher_t, s):
    plain_t = ""
    for char in cipher_t:
        if char.isupper():
            plain_t += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            plain_t += chr((ord(char) - s - 97) % 26 + 97)
        else:
            plain_t += char  # leave non-alphabetic characters unchanged
    return plain_t

text = input("Enter the text to encrypt: ")
s = 3
print("Text: " + text)
encrypted_text = encrypt(text, s)
print("Cipher: " + encrypted_text)
decrypted_text = decrypt(encrypted_text, s)
print("Plain: " + decrypted_text)
