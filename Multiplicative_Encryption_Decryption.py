#Multiplicative Encryption Program in python
a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def KeyInput():
    key=int(input("Enter key value:"))
    if key%2==0:
        print(f"There is no modular multiplicative inverse for {key}")
        key=KeyInput()
        return key
    else:
        return key
key=KeyInput()
PlainText=str(input("Enter message without space:"))
P_T=PlainText.upper()
print("\nUser message in plain text: ",P_T)
#spliting the string using list function
PT_split=list(P_T)
print("Splited string:",PT_split)

l=[]
for i in range(len(PT_split)):
    l.append(int(a.index(PT_split[i])))
print(l)

b=[]
for i in range(len(l)):
    if l[i]*key<=25:
        b.append(l[i]*key)
    else:
        R=(l[i]*key)% 26
        b.append(R)
print(b)
F=[]
for i in range(len(b)):
    F.append(a[int(b[i])])
print(F)

CT=""
CT=(CT.join(F))
print("\n Encrypted Message:",CT)

#Decryption program
Ciphertext=CT
C_T=Ciphertext.upper()
print("Given Ciphertext is: ",C_T)
CT_split=list(C_T)
print(CT_split)

Q=[]
for i in range(len(CT_split)):
    Q.append(int(a.index(CT_split[i])))
print(Q)

def key_inverse(k):
    i=1
    while i>0:
        #print(i)
        if(k*i)%26==1:
            key_inv=i
            #if k!=key_inv:
               #return key_inv
            break
        else:
            i+=1
    return key_inv      
    

print("Key value:",key)
key_Inv=key_inverse(key)
print("Key inverse:",key_Inv)

P=[]
for i in range(len(Q)):
    
    if((Q[i]*key_Inv)<=25):
        P.append(Q[i]*key_Inv)
    else:
        P.append((Q[i]*key_Inv)%26)
    
print(P)
DC=[]
for i in range(len(P)):
    DC.append(a[int(P[i])])
print(DC)

DCT=""
DCT=(DCT.join(DC))
print("\n Decrypted Message: ",DCT)



