import hashlib
result = hashlib.md5(b'Computer')
result1 = hashlib.md5(b'Science')
# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
print("The byte equivalent of hash is : ", end ="")
print(result1.digest())

import hashlib
str = input(" Enter the value to encode ")
result = hashlib.sha1(str.encode())
print("The hexadecima equivalent if SHA1 is :  ")
print(result.hexdigest())
