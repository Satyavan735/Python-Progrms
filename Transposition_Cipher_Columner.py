#Transposition Cipher Columner
import numpy as np
Plain_Text=str(input("Enter Your Message:"))
U=Plain_Text.upper()
#PT_Split=list(U)
col=int(input("\nEnter Key:"))
#print(PT_Split)
S=[]
p1=[]
for i in range(0,len(U),col):
    p1.append(list(U[i:i+col]))

print("\nSplited list:")
print(p1)
l=[]
for i in range(len(p1)):
    if col>len(p1[len(p1)-1]):
        diff=len(p1[0])-len(p1[len(p1)-1])
        for i in range(diff):
            p1[len(p1)-1].append('$')
    
col_len=len(Plain_Text)//col       
if(col_len%col!=0):
    col_len+=1
print("\nSplited list after appending $:")
print(p1)
print(np.matrix(p1))

CT=[]
def TransposeMat(row,cl,ele):
    for i in range(row):
        u=[]
        for j in range(cl):
            u.append(ele[j][i])
        CT.append(u)
TransposeMat(len(p1[0]),col_len,p1)
print("\nPrinting Transpose matrix:")
print(np.matrix(CT))

#Join list
for i in range(len(CT)):
    l+=CT[i]
print(l)
#Join alphabets
en=""
en=en.join(l)
print("\nEncrypted message: ",en)

#Decryption of Columner Cipher
C_T=en
key=col
Columns=len(C_T)//key

MX=[]
for i in range(0,len(C_T),Columns):
    MX.append(list(C_T[i:i+Columns]))

CT=[]
def TransposeMat(row,cp,ele):
    for i in range(cp):
        u=[]
        for j in range(row):
            u.append(ele[j][i])
        CT.append(u)
TransposeMat(key,Columns,MX)
print("\nPrinting Transpose matrix:")
print(np.matrix(CT))

E=[]
#Join list
for i in range(len(CT)):
    E+=CT[i]
print(E)

Final_li=[]
for i in E:
    if i!='$':
        Final_li.append(i)
        

#Join alphabets
en=""
en=en.join(Final_li)
print("\nDecrypted message: ",en)












