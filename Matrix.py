#PracticalNo:01
"""
c1=complex(input("Enter First complex number:"))
c2=complex(input("Enter second complex number:"))

print("Addition",c1+c2)
print("Subtraction",c1-c2)
print("Multiplication",c1*c2)
print("Division",c1/c2)
print("conjugate of c1",c1.conjugate())
print("conjugate of c2",c2.conjugate())
from cmath import sqrt 
print("Square root of c1",sqrt(c1))
print("Square root of c2",sqrt(c2))
"""
#Practical No:02
"""
import matplotlib.pyplot as plt
C={2+3j,5+6j,7+8j,6+3j,4+2j,5+7j}
print("Complex numbers are:",C)
P=[x.real for x in C]
print("Real part of complex number is:",P)
Q=[x.imag for x in C]
print("Imaginary number",Q)
plt.plot(P,Q)
plt.show()

import matplotlib.pyplot as plt
print("Rotation throught 90 degree")
C={2+3j,5+6j,7+8j,6+3j,4+2j,5+7j}
C1=[x*1j for x in C]

P=[x.real for x in C1]
print("Real part",P)
Q=[x.imag for x in C1]
print("Imag part of complex number",Q)
plt.plot(P,Q)
plt.show()

import matplotlib.pyplot as plt
print("Rotation throught 180 degree")
C={2+3j,5+6j,7+8j,6+3j,4+2j,5+7j}
C1=[x*-1 for x in C]

P=[x.real for x in C1]
print("Real part",P)
Q=[x.imag for x in C1]
print("Imag part of complex number",Q)
plt.plot(P,Q)
plt.show()


import matplotlib.pyplot as plt
print("Rotation throught 180 degree")
C={2+3j,5+6j,7+8j,6+3j,4+2j,5+7j}
C1=[x*2 for x in C]

P=[x.real for x in C1]
print("Real part",P)
Q=[x.imag for x in C1]
print("Imag part of complex number",Q)
plt.plot(P,Q)
plt.show()




#Practical No 03:
def Scalar_V_M(A,B,C,D):
    return[C*A[i]+B[i]*D for i in range(len(A))]

def Add(A,B):
    return[A[i]+B[i] for i in range(len(A))]

def vecAvg(Add,NoOfvector):
    return[Add[i]/NoOfvector for i in range(len(Add))]

m=[]
R=int(input("Enter row:"))
for i in range(R):
        m.append(int(input("Enter value: ")))
        
print(m)

m1=[]
R1=int(input("Enter row:"))
for i in range(R1):
        m1.append(int(input("Enter value: ")))
Noofvector=2       
print(m1)
S1=int(input("Enter first scalar:"))
S2=int(input("Enter second scalar:"))
print("Scalar vector multiplication and vectro vector addition",Scalar_V_M(m,m1,S1,S2))
print("Addition of two vwctor:",Add(m,m1))
RAdd=Add(m,m1)
print("Average",vecAvg(RAdd,Noofvector))


#practical no 04

from PIL import Image
import numpy as np

def Image_Size(Img,Size):
    Img1=Image.fromarray(Img)
    return np.array(Img1.resize(Size))

Im1=Image.open("D:\Satyavan\Galaxy.jpg")
Im1.show()
Im2=Image.open("D:\Satyavan\Kedarnath.jpg")
Im2.show()

a1=np.array(Im1)
a2=np.array(Im2)

P=Image_Size(a1,(900,600))
Q=Image_Size(a2,(900,600))

Add=P+Q

linimg=Image.fromarray(Add.astype('uint8'))
linimg.show()

lincomb=Add/2
linimg=Image.fromarray(lincomb.astype('uint8'))
linimg.show()

"""
#Practical no 07
import numpy as np
def vector_matrix(vector,mat):
    Result=[]
    for i in range(len(mat[0])):
        Total=0
        for j in range(len(vector)):
            Total+=vector[j]*mat[j][i]
        Result.append(Total)

    print(Result)
    

v=[2,3]
Mat=[[1,2,4],
     [10,15,20]]

vector_matrix(v,Mat)










