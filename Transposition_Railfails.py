#Transposition cipher Rail Fence
Plain_Text=str(input("Enter Your Message:"))
U=Plain_Text.upper()
PT_Split=list(U)
#print(PT_Split)
PT_Split_Odd=[]
PT_Split_Even=[]
for i in range(len(PT_Split)):
    if (i)%2==0:
        PT_Split_Odd.append(PT_Split[i])
    else:
        PT_Split_Even.append(PT_Split[i])

if(len(PT_Split_Even)!=len(PT_Split_Odd)):
    G_list=(len(PT_Split_Even)>len(PT_Split_Odd))

    if G_list:
            PT_Split_Odd.append('$')
    else:
            PT_Split_Even.append('$')

print("\nEven index array: ",PT_Split_Even)
print("\nOdd index array: ",PT_Split_Odd) 
CT=[]
for i in range(len(PT_Split_Even)):
    CT.append(PT_Split_Odd[i])
      
for i in range(len(PT_Split_Odd)):
    CT.append(PT_Split_Even[i])  
       

P_CT=""
P_CT=(P_CT.join(CT))
print("\n Encrypted Message:",P_CT)

#Decryption program
Cipher_Text=P_CT

CT_Split=list(Cipher_Text)

#Find middle index of list and split it
Mid_index=len(CT_Split)//2
CT_Split_Odd=CT_Split[:Mid_index]
CT_Split_Even=CT_Split[Mid_index:] 
print("\nEven index array: ",CT_Split_Even)
print("\nOdd index array: ",CT_Split_Odd) 
A=[]
for i in range(len(CT_Split_Even)):
    A.append(CT_Split_Odd[i])
    A.append(CT_Split_Even[i])
#print(A)
if(A[len(A)-1]=='$'):
    A.pop()

PT=""
PT=(PT.join(A))
print("\nDecrypted Message:",PT)



