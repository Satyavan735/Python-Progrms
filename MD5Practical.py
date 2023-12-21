#Python program to demonstrate working of MD5 algorithm.
import hashlib
#Encoding the string using md5 hash function

PT="Bootstrap"
result=hashlib.md5(b'Bootstrap')

#printing the equivalent byte value.

print(f"The byte equivalent of {PT} is : ",end="")
print(result.digest())

Text="Bootstrap"
#Encoding Bootstrap using encode()
Res=hashlib.md5(Text.encode())

# printing the equivalent hexadecimal value.
print(f"The hexadecimal equivalent of {PT} is : ", end ="")
print(Res.hexdigest())