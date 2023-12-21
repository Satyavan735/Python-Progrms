#Playfair cipher program
import numpy as np
P_Mat=[['L','G','D','B','A'],
       ['Q','M','H','E','C'],
       ['U','R','N','I','F'],
       ['X','V','S','O','K'],
       ['Z','Y','W','T','P']]

PT=str(input("Enter your Message:"))
U=PT.upper()
#For Checking J alphabet  is present in text 
for i in U:
    if i=='J':
        P_Mat[2][3]='J'

Mat=np.matrix(P_Mat)
print(Mat)
PT_li=list(U)
print(PT_li)
Split1=[]
for i in range(len(PT_li)):
    Split1.append(PT_li[i:i+2])
Split1[len(Split1)-1].append(Split1[0][0])
print(Split1)
print(len(Split1))
#Split down list into two segments
Row=[]
Column=[]
def Search_Ele(M,var,FS):
    for i in range(len(P_Mat)):
        for j in range(len(P_Mat[0])):
            if M[i][j]==var:
                if FS:
                    Row.append([i,j])
                    
                else:
                    Column.append([i,j])
                    
                    
        
for i in range(len(Split1)):
    for j in range(len(Split1[0])):
        if j==0:
            F=True
            v=Split1[i][j]
            Search_Ele(P_Mat,v,F)
        else:
            F=False
            v1=Split1[i][j]
            Search_Ele(P_Mat,v1,F)

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

#To check element is last in row or not
def Check_Ele(I1,R,C):
    if R==4:
        Ele.append(P_Mat[I1][0])
    if C==4:
        Ele.append(P_Mat[I1][0])

#To check element is last in column or not
def Check_Ele_Col(I1,R,C):
    if R==4:
        Ele.append(P_Mat[0][I1])
    if C==4:
        Ele.append(P_Mat[0][I1])
Ele=[]
def Search_CipherEle(I1,R,C,S_Row,S_Col,both):
    if S_Row:
        if R>C:
            Check_Ele(I1,R,C)
            if R!=4 and C!=4:
                H=R+1
                Ele.append(P_Mat[I1][H])
        if C>R:
            Check_Ele(I1,R,C)
            if R!=4 and C!=4:
                H=C+1
                Ele.append(P_Mat[I1][H])
    elif S_Col:
        if R>C:
            Check_Ele_Col(I1,R,C)
            if R!=4 and C!=4:
                H=R+1
                Ele.append(P_Mat[H][I1])
        if C>R:
            Check_Ele_Col(I1,R,C)
            if R!=4 and C!=4:
                H=C+1
                Ele.append(P_Mat[H][I1])
    elif both:
        Check_Ele_Col(C,R,None)
        if R!=4:
            R+=1
            Ele.append(P_Mat[R][C])

    else:
        Ele.append(P_Mat[R][C])

            
Col=""
row=""
for i in range(0,len(S)-1,2):
    if(S[i]==T[i] and S[i+1]==T[i+1]):#Row and Column
        Both=True
        Search_CipherEle(None,S[i],S[i+1],None,None,Both)
    elif (S[i]==T[i]) and i%2==0:#For Row
        row=True
        Col=False
        a=i+1
        Search_CipherEle(S[i],S[a],T[a],row,Col,None)
    elif (S[i+1]==T[i+1])and i+1%2!=0:#For Column
        Col=True
        row=False
        Search_CipherEle(S[i+1],S[i],T[i],row,Col,None)
    
    else:   
        Search_CipherEle(None,S[i],T[i+1],None,None,None)

        
C_Text=""
C_Text=C_Text.join(Ele)
print("\nEncrypted message:",C_Text)