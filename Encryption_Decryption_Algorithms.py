#Additive Encryption Program in python
a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

key=int(input("Enter key value:"))
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
    if l[i]+key<=25:
        b.append(l[i]+key)
    else:
        R=(l[i]+key)% 26
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

P=[]
for i in range(len(Q)):
    if Q[i]>key:
        P.append(Q[i]-key)
    else:
        T=((Q[i]+26)-key)
        P.append(T)
print(P)
DC=[]
for i in range(len(P)):
    DC.append(a[int(P[i])])
print(DC)

DCT=""
DCT=(DCT.join(DC))
print("\n Decrypted Message: ",DCT)



