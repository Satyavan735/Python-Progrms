#Permutation Cipher program
PT=str(input("Enter your message:"))
key=int(input("Enter total number of position you want to change:"))
checkkey=[]
for i in range(key):
    checkkey.append(i+1)
#print(checkkey)
#print(max(checkkey))
print("\nEnter keys:")
print(f"Enter key value from 1 to {key}")
key_li=[]
def Keys():
    for i in range(key):
        k_U=int(input(f"Enter {i+1} key value:"))
        if k_U>max(checkkey):
            print(f"\nPlease re-enter key value between 1 to {key}")
            i=0
            key_li.clear()
            Keys()
            break
            
        else:
            key_li.append(k_U)
Keys()
print("\nKeys list:",key_li)

upper=PT.upper()
PT_Split=list(upper)
print("\nPlain Text list:")
print(PT_Split)
#split list according to number of keys value
PT_Split1=[]
for i in range(0,len(PT_Split),key):
    PT_Split1.append(PT_Split[i:i+key])
print("\nSplited list:")
print(PT_Split1)

for i in range(len(PT_Split1)):
    if key>len(PT_Split1[i]):
        dif=key-len(PT_Split1[i])
        for i in range(dif):
            PT_Split1[len(PT_Split1)-1].append('$')
print("\n List after appending '$'")
print(PT_Split1)
CT=[]
def Search_ele(Sub_li,K_li):
    for i in range(len(Sub_li)):
        CT.append(Sub_li[K_li[i]-1])

for i in PT_Split1:
    Search_ele(i,key_li)

CipherText=""
CipherText=CipherText.join(CT)
print("\nEncrypted message:",CipherText)

#Decryption program
EN=list(CipherText)
print(EN)
Key=key_li
Split_val=len(Key)
En_li=[]
for i in range(0,len(EN),Split_val):
    En_li.append(EN[i:i+Split_val])
print(En_li)

PT_Search=[]
def Search_ele1(Subli,K_li):
    for i in range(len(Subli)):
            PT_Search.append(Subli[K_li[i]-1])
        


for i in En_li:
    Search_ele1(i,Key)

print(PT_Search)

