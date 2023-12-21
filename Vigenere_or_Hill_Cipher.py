#Vigenere cipher algorithm
import numpy as np
#      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
Reg=[['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
    ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A'],
    ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B'],
    ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C'],
    ['E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D'],
    ['F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E'],
    ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F'],
    ['H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G'],
    ['I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H'],
    ['J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I'],
    ['K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J'],
    ['L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K'],
    ['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L'],
    ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M'],
    ['O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N'],
    ['P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'],
    ['Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
    ['R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],
    ['S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'],
    ['T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S'],
    ['U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'],
    ['V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'],
    ['W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'],
    ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'],
    ['Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'],
    ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']]



PlainText=str(input("Enter your message: "))
U=PlainText.upper()
PT_li=list(U)
print(PT_li)
key=[]
#print(len(PT_li))
for i in range(len(PT_li)):
    if i==len(PT_li)-1:
        key.append(PT_li[0])
    else:
        key.append(PT_li[i+1])
print(key)
Split1=[]
for i in range(len(PT_li)):
    Split1.append(PT_li[i:i+2])
Split1[len(Split1)-1].append(Split1[0][0])
print(Split1)


#Split down list into two segments
Row=[]
Column=[]
def Search_Ele(M,var,FS):
    for i in range(len(Reg)):
        for j in range(len(Reg[0])):
            if M[i][j]==var:
                if FS:
                    Row.append([j,i])
               
                else:
                    Column.append([i,j])
        break           

               
       
for i in range(len(Split1)):
    for j in range(len(Split1[0])):
        if j==0:
            F=True
            v=Split1[i][j]
            Search_Ele(Reg,v,F)
        else:
            F=False
            v1=Split1[i][j]
            Search_Ele(Reg,v1,F)

        #print(i ," ",j)


print("Row values:",Row)
print("Colum values:",Column)

S=[]
T=[]
for i in range(len(Row)):
    S+=Row[i]
    T+=Column[i]
print(S)
print(T)
Ele=[]
def Search_CipherEle(R,C):
    Ele.append(Reg[R][C])

C=""
R=""
for i in range(0,len(S)-1,2):
    if S[i+1]==0:
        F=True
        R=S[i]
        C=T[i+1]
        Search_CipherEle(R,C)

CipherText="".join(Ele)   
print("Encrypted Text:",CipherText)

#Decryption Algorithm
CT=CipherText
DecKey=key
print("Decryption Key: ",DecKey)
Ele_Row=[]
def SearchRow(Key):
    for i in range(len(Reg)):
        for j in range(len(Reg[0])):
            if Reg[i][j]==Key:
                li=[]
                li+=Reg[j]
                if Key==li[0]:
                    Ele_Row.append(Reg[j])
                    

for i in DecKey:
    SearchRow(i)

#print(Ele_Row)
PT=[]
def plaintext(colind):
    for i in range(len(Reg)):
        PT.append(Reg[0][colind])
        break

#Search Diagonal Element
def SearchColumn(Col,key_l,First_Row):
    for i in range(len(First_Row)):
        if First_Row[i]==Col:
            col_ind=i
            #print(col_ind)
            plaintext(col_ind)
            
for i in range(len(DecKey)):
    SearchColumn(CT[i],DecKey[i],Ele_Row[i])      

DecryptedMessage="".join(PT)
print("Decrypted Message: ",DecryptedMessage)