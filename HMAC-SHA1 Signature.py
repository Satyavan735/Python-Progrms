#Python program to demonstrate working of hmac module.

import hmac
import hashlib
#Creating a new hmac object using sha1 hash algorithm

hmac_obj=hmac.new(b'privatekey',b'Satyavan',hashlib.sha1)

#print the Hexdigest of the bytes passed to update
print("Hexdigest: "+hmac_obj.hexdigest())

#Calling update to update the msg
hmac_obj.update(b'another msg')

#print the Hexdigest of the bytes passed to update
print("Hexdigest After Update: "+hmac_obj.hexdigest())

print("Digest size:"+str(hmac_obj.digest_size)+"bytes")
print("Block size: "+str(hmac_obj.block_size)+"bytes")
print("Canonical name:"+hmac_obj.name)

#print digest of bytes passed to update
print("Digest value: ",end="")
print(hmac_obj.digest())

#Create a copy of hmac object
hmac_copy=hmac_obj.copy()
print("Hexdigest of clone/copy: "+hmac_copy.hexdigest())
