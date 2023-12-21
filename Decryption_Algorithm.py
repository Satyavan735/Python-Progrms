#Decryption program
a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

print(a)
print(a[0])

key=int(input("Enter key value:"))
PlainText=str(input("Enter message without space:"))
P_T=PlainText.upper()
print(P_T)
PT_split=list(P_T)
print(PT_split)

print(PT_split[0])
l=[]
for i in range(len(PT_split)):
    l.append(int(a.index(PT_split[i])))
print(l)

b=[]
for i in range(len(l)):
    if l[i]>key:
        b.append(l[i]-key)
    else:
        R=((l[i]+26)-key)
        b.append(R)
print(b)
F=[]
for i in range(len(b)):
    F.append(a[int(b[i])])
print(F)

CT=""
CT=(CT.join(F))
print(CT)


