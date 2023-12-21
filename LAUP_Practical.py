"""
Name : Satyavan Dhaku Mestry .
Roll No : 27
Class: S.Y.Bsc Computer Science
Linear Algebra using Python Practical  No:01
01)Basic operation on complex number

C1=complex(input("Enter first complex number:"))
C2=complex(input("Enter second complex number:"))
print(f"Complex numbers are {C1} and {C2}")
#Addition of complex number ṇ
print(f"Addition of {C1} and {C2} is",C1+C2)
#Subtraction of complex number 
print(f"Subtraction of {C1}and {C2} is",C1-C2)
#Multiplication of complex number 
print(f"Multiplication of {C1} and {C2} is",C1*C2)
#Division of complex number 
print(f"Division of {C1}and {C2} is",C1/C2)
#Conjugate of complex number
print(f"Conjugate of {C1} is :" ,C1.conjugate())
print(f"Conjugate of {C2} is:",C2.conjugate())
#Square root of complex numbers 
from cmath import sqrt
print(f"Square root of {C1} is :",sqrt(C1))
print(f"Square root of {C2} is :",sqrt(C2))

"""
Name : Satyavan Dhaku Mestry .
Roll No : 27
Class: S.Y.Bsc Computer Science
Linear Algebra using Python Practical  No:02
Q1)Creating a new plot by rotating the given number by a degree 90,
 180 degrees and also by scaling by a number a=1/2, a=1/3, a=2 etc.
"""
"""
#Plotting of complex numbers
#Create a new plot by rotating the given set by 90,180 degree
import matplotlib.pyplot as plt
C={2+3j,4+6j,3+3j,7+8j,5+7j,3+9j}
print("Complex numbers are :",C)
P=[x.real for x in C]
print("Real part of complex numbers:",P)
Q=[x.imag for x in C]
print("Imag part of complex numbers:",Q)
plt.plot(P,Q)
plt.show()


#Rotation through 90 degrees
import matplotlib.pyplot as plt
C={2+3j,4+6j,3+3j,7+8j,5+7j,3+9j}
print("Complex numbers are :",C)
C1=[x*1j for x in C]
print("After rotation through 90 degrees complex numbers are:",C1)
P=[x.real for x in C1]
print("Real part of complex numbers:",P)
Q=[x.imag for x in C1]
print("Imag part of complex numbers:",Q)
plt.plot(P,Q)
plt.show()

#Rotation through 180 degrees
import matplotlib.pyplot as plt
C={2+3j,4+6j,3+3j,7+8j,5+7j,3+9j}
print("Complex numbers are :",C)
C1=[x*-1 for x in C]
print("After rotation through 180 degrees complex numbers are:",C1)
P=[x.real for x in C1]
print("Real part of complex numbers:",P)
Q=[x.imag for x in C1]
print("Imag part of complex numbers:",Q)
plt.plot(P,Q)
plt.show()

#Plotting of complex numbers
#Scaling by a number a=1/2, a=1/3, a=2
import matplotlib.pyplot as plt
C={2+3j,4+6j,3+3j,7+8j,5+7j,3+9j}
a=2
print("Complex numbers are :",C)
C1=[x*a for x in C]
print("After rotation through 180 degrees complex numbers are:",C1)
P=[x.real for x in C1]
print("Real part of complex numbers:",P)
Q=[x.imag for x in C1]
print("Imag part of complex numbers:",Q)
plt.plot(P,Q)
plt.show()

Name : Satyavan Dhaku Mestry .
Roll No : 27
Class: S.Y.Bsc Computer Science
Linear Algebra using Python Practical  No:03
3. Write a program to do the following:
• Enter two distinct faces as vectors u and v.
• Find a new face as a linear combination of u and v i.e. au+bv for a and b in R.
• Find the average face of the original faces.

#Scalar vector multiplication and vector vector addition 
def Scalar_Vector_Mul_ADD(A,B,C,D):
    return[C*A[i]+D*B[i] for i in range(len(A))]

#Finding average face of original faces
#Vector Addition
def Vadd(x,y):
    return [x[i]+y[i] for i in range(len(x))]
#Vector Average
def Vavg(M,N):
    return[M[i]/N for i in range(len(M))]

# creating an empty first vector
T = []

# number of elements as input for vector
n = int(input("Enter number of elements of first vector: "))

# iterating till the range of vector
for i in range(0, n):
	ele = int(input(f"Enter {i+1} element:"))

	T.append(ele) # Appending the values of vector elements
No_of_vector=1
# creating an empty second vector
W = []

# number of elements as input for vector
n = int(input("Enter number of elements of second vector: "))

# iterating till the range of vector
for i in range(0, n):
	ele = int(input(f"Enter {i+1} element:"))

	W.append(ele) # Appending the values of vector elements
No_of_vector+=1    
X=int(input("Enter value of  First Scalar:"))
Y=int(input("Enter value of Second Scalar:"))

print(f"\nScalar vector multiplication and vector vector addition of {T} and {W} is:\n",Scalar_Vector_Mul_ADD(T,W,X,Y))
print(f"\nNumber of vector is:{No_of_vector}")
ADD_V=Vadd(T,W)
print(f"Addition of {T} and {W} is:",ADD_V)
print(f"\nAverage of {T} and {W} is:",Vavg(ADD_V,No_of_vector))


#Vector Addition
def Vadd(x,y):
    return [x[i]+y[i] for i in range(len(x))]
S=[1,2,3,6]
R=[0,9,8,4]
print(f"\nAddition of {S} and {R} is:",Vadd(S,R))

#Vector subtraction 
def Vsub(x,y):
    return [x[i]-y[i] for i in range(len(x))]
P=[1,2,3,6]
Q=[0,9,8,4]
print(f"\nSubtraction of {P} and {Q} is:",Vsub(P,Q))

#Scalar vector multiplication
def Vmul(X,a):
    return[a*X[i] for i in range(len(X))]
D=[1,2,3,6]
print(f"\nScalar vector multiplication  of {D} and 2 is :",Vmul(D,2))

#Dot product
def DotProduct(A,B):
    return sum([A[i]*B[i] for i in range(len(A))])
G=[1,2,3,6]
H=[0,9,8,4]
print(f"\nDot product of{G} and {H} is: ",DotProduct(G,H))



#Vector operations using numpy
import numpy as np
A=np.array([2,4,4,2])
B=np.array([4,2,2,4])
print(f"\nAddition of {A} and {B} using numpy is:",A+B)
#Dot product
F=print(f"\nDot product of {A} and {B} is:",np.dot(A,B))

print(f"\nAddition of {A} and {B} using function in numpy is:",np.add(A,B))

Circle Program
from numpy import *
import matplotlib.pyplot as plt
R=2+3j
t=arange(0,2*pi,.01)
x=R*sin(t)
y=R*cos(t)
plt.plot(x,y)
plt.xlabel('t {s}')
plt.ylabel('y {m}')
plt.show()

Name : Satyavan Dhaku Mestry .
Roll No : 27
Class: S.Y.Bsc Computer Science
Linear Algebra using Python Practical  No:04
4. Write a program to do the following:
• Enter an r by c matrix M (r and c being positive integers)
• Display M in matrix format
• Display the rows and columns of the matrix M
• Find the scalar multiplication of M for a given scalar.
• Find the transpose of the matrix M.


import numpy as np

No_Row = int(input("Enter the number of rows:"))
No_Column = int(input("Enter the number of columns:"))


print("Enter the entries in a single line for matrix: ")

# User input in a single line 
Entries = list(map(int, input().split()))

# For printing the matrix
M= np.array(Entries).reshape(No_Row,No_Column)
print("Matrix form is:")
print(M)
print("\n")  
#Printing Rows of Matrix M
print("Printing rows of matrix M")
for i in range(len(M)):
    print(f"{i+1} row:",M[i])

print("\n")    
#Printing Columns of Matrix M 
print("Printing columns of matrix M")  
for i in range(0,len(M)):
    print(f"{i+1} column is:",M[:,i])  
    
#Find the scalar multiplication of M for a given scalar.
Scalar=int(input("Enter a scalar:"))
print("Scalar multiplication of :") 
print(M)
print(f"\n With {Scalar} is :")
print(M*Scalar)

# Find the transpose of the matrix M.
print("\nPrinting transpose of the matrix M ")
T=M.transpose()
print(T)


#Matrix Program
import numpy as np
print("Print Matrix using array")
A=np.array([[1,2,2],[2,3,4]])
print(A)
print("\nPrint Matrix using matrix function") 
B=np.matrix([[1,2],[2,4]])
print(B)
import numpy.matlib
import numpy as np
print("\nPrint matrix with matlib ")
C=np.matlib.zeros((2,3))
print(C)
print(np.matlib.ones((4,4)))
print("\nPrint identity matrix")
I=print(np.matlib.identity(3,dtype=int))
print(np.matlib.identity(5,dtype=int))

# Print like array: D=np.mat('1,2,3,4')
print("\nPrint matrix with mat function")
D=np.mat('1,2;3,4')
print(D)



import numpy as np
import numpy.matlib
print("Addition of matrix using add function")
a=np.mat('1,3,5;2,4,6;1,6,8')
print(a)
b=np.mat('0,2,1;3,4,5;-1,-2,3')
print(b)
print("\nAddition is:")
print(np.add(a,b))
#print(a+b)
print("\nSubtraction of matrix:")
print(np.subtract(a,b))
#print(a-b)
print("\n")
c=np.mat('1,-2;3,-1')
print(c)
d=np.mat('1,0;-1,1')
print(d)

print("\nMultiplication of Matrix")
print(c*d)
print("\nmultiplication by Dot product")
print(np.dot(c,d))
print("\nMatrix term by term multiplication")
print(np.multiply(c,d))
print("\nScalar matrix  multiplication ")
r=3
x=print(3*d)
print("\nTranspose of matrix")
print(np.transpose(a))
print("\nTranspose with T")
print(a.T)
print("\nInverse of matrix")
f=np.mat('1,2;2,-1')
print(f)
print(np.linalg.inv(f))
print("\nInverse of identity matrix")
I=np.matlib.identity(3,dtype=int)
print(I)
print(np.linalg.inv(I))
print("\n")
t=np.mat('4,3;3,2')
print(t)
print(np.linalg.inv(t))


#Practi
print("Solving triangular system")
import numpy as np
from scipy.linalg import solve_triangular
A=np.mat('5,3,-2;0,-11,-5;0,0,1')
print(A,"\n")
c=np.array([0,10,15])
print(c,"\n")
s=solve_triangular(A,c,lower=False)
print(s,"\n")

A=np.mat('1,0,0;0,4,2;6,5,1')
print(A,"\n")
c=np.array([0,0,0])
print(c,"\n")
s=solve_triangular(A,c,lower=False)
print(s)


#Practical No 05
#5. Write a program to do the following:
# Find the vector –matrix multiplication of a r by c matrix M with an c-vector u.
# Find the matrix-matrix product of M with a c by p matrix N. 

#Defining a function to print vector matrix multiplication

def vectormatrixmul(A,V):
    C=[sum(V[j]*A[j][i] for j in range(len(V))) for i in range(len(A)) ]
    print(C)

r=int(input("Enter number of rows:"))
c= int(input("Enter the number of columns:"))

Mat= []
print("Enter elements in matrix:")

for i in range(r):
    A =[]
    for j in range(c):
         A.append(int(input()))
    Mat.append(A)
 
for i in range(r):
    for j in range(c):
        print(Mat[i][j], end = " ")
    print()
T=[]
n = int(input("Enter number of elements of vector: "))

for i in range(0, n):
	ele = int(input(f"Enter {i+1} element:"))

	T.append(ele) # Appending the values of vector elements

print(T)   

vectormatrixmul(Mat,T)    


#Name : Satyavan Dhaku Mestry .
#Roll No : 27
#Class: S.Y.Bsc Computer Science
#Linear Algebra using Python Practical  No:03
#3. Write a program to do the following:
#• Enter two distinct faces as vectors u and v.
#• Find a new face as a linear combination of u and v i.e. au+bv for a and b in R.
#• Find the average face of the original faces.
#Image Practical 
#Addition of two images
from PIL import Image
import numpy  as np

def ImageSize(Img,Size):
    Img1=Image.fromarray(Img)
    return np.array(Img1.resize(Size))

Im1=Image.open('D:\Satyavan\Wallpaper\star.jpg')
Im1.show()

Im2=Image.open('D:\Satyavan\Wallpaper\stars-wallpaper-16.jpg')

Im2.show()

a1=np.array(Im1)
a2=np.array(Im2)

p=ImageSize(a1,(900,600))
q=ImageSize(a2,(900,600))

Add=p+q

Linimg=Image.fromarray(Add.astype('uint8'))
Linimg.show()

"""
#Name : Satyavan Dhaku Mestry .
#Roll No : 27
#Class: S.Y.Bsc Computer Science
#Linear Algebra using Python Practical  No:03
#3. Write a program to do the following:
#• Enter two distinct faces as vectors u and v.
#• Find a new face as a linear combination of u and v i.e. au+bv for a and b in R.
#• Find the average face of the original faces.
#Image Practical 
#Average of two images
from PIL import Image
import numpy  as np

def ImageSize(Img,Size):
    Img1=Image.fromarray(Img)
    return np.array(Img1.resize(Size))

Im1=Image.open('D:\Satyavan\Wallpaper\star.jpg')
Im1.show()

Im2=Image.open('D:\Satyavan\Wallpaper\stars-wallpaper-16.jpg')

Im2.show()

a1=np.array(Im1)
a2=np.array(Im2)

p=ImageSize(a1,(900,600))
q=ImageSize(a2,(900,600))

Add=p+q
lincomb=Add/2

Linimg=Image.fromarray(lincomb.astype('uint8'))
Linimg.show()




"""

#Name : Satyavan Dhaku Mestry .
#Roll No : 27
#Class: S.Y.Bsc Computer Science
#Linear Algebra using Python Practical  No:05
#5. Write a program to do the following:
#• Find the matrix-matrix product of M with a c by p matrix N.
#Matrix Matrix Multiplication
import numpy as np
def Matrix_Matrix_Mul(A,B):
    C=[[0 for row in range(len(A))]for col in range(len(B))]
    np.array(C)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]
        print(C[i],"\n")
Mat1=[]
R=int(input("\nEnter number of rows in matrix:"))
C=int(input("\n Enter number of columns in matrix:"))

for i in range(R):
    A=[]
    for j in range(C):
        A.append(int(input(f"Enter an {j+1} element of matrix:")))
    Mat1.append(A)

print("\n First  Matrix is:")
for i in range(R):
    for j in range(C):
        print(Mat1[i][j],end=" ")
    print()
Mat2=[]
R=int(input("\nEnter number of rows in matrix:"))
C=int(input("\n Enter number of columns in matrix:"))

for i in range(R):
    A=[]
    for j in range(C):
        A.append(int(input(f"Enter an {j+1} element of matrix:")))
    Mat2.append(A)

print("\n Second Matrix is:")
for i in range(R):
    for j in range(C):
        print(Mat2[i][j],end=" ")
    print()
    
print("\n  Matrix-Matrix Multiplication is:")
  
Matrix_Matrix_Mul(Mat1,Mat2)






#Name : Satyavan Dhaku Mestry .
#Roll No : 27
#Class: S.Y.Bsc Computer Science
#Linear Algebra using Python Practical  No:05
#5. Write a program to do the following:
# Find the vector –matrix multiplication of a r by c matrix M with an c-vector u.
#Vector Matrix Multiplication 
import numpy as np
def Vector_Matrix_Mul(vector,Mat):
    Result=[]
    for i in range(len(Mat[0])):
        Total=0
        for j in range(len(vector)):
            Total+=vector[j]*Mat[j][i]
        Result.append(Total)
    print("\nVector -Matrix Multiplication is:")
    print("\n",Result)

Vector=[]
VLength=int(input("Enter number of element in vector:"))

for v in range(VLength):
    i=v+1
    Vector.append(int(input(f"Enter {i} element: ")))
    
print("\n Given Vector is:",Vector)


Mat=[]
R=int(input("\nEnter number of rows in matrix:"))
C=int(input("\n Enter number of columns in matrix:"))

for i in range(R):
    A=[]
    for j in range(C):
        A.append(int(input("Enter an element of matrix:")))
    Mat.append(A)

print("\n Given Matrix is:")
for i in range(R):
    for j in range(C):
        print(Mat[i][j],end=" ")
    print()

Vector_Matrix_Mul(Vector,Mat)




#Name : Satyavan Dhaku Mestry .
#Roll No : 27
#Class: S.Y.Bsc Computer Science
#Linear Algebra using Python Practical  No:08
#8. Write a program to do the following:
#• Find the gcd of two numbers using Euclid’s algorithm.
#GCD Program
A=int(input("Enter 1st number:"))
B=int(input("Enter second number:"))  
  #GCD calculation program
def GCD(a,b):
    if a>b:
        if b!=0:
            if a % b==0:
                print(f"\n GCD of{A} and {B} is: ",b)
            else:
                r=a % b
                GCD(b,r)
        else:
            print("\n Second number must be greater than zero..")
    else:
        GCD(b,a)
            
GCD(A,B)




#6. Write a program to enter a matrix and check if it is invertible. 
#If the inverse exists, find the inverse. 
import numpy as np
import numpy.matlib

print("\nInverse of matrix")
f=np.mat('1,2;2,-1')
print("\nGiven matrix is:")
print(f)
print("\n Inverse id matrix is:")
print(np.linalg.inv(f))
print("\nInverse of identity matrix")
I=np.matlib.identity(3,dtype=int)
print(I)
print("\nInverse of identity matrix is:")
print(np.linalg.inv(I))
print("\n")
print("\n Given matrix is:")
t=np.mat('4,3;3,2')
print(t)
print("\nInverse of matrix is:")
print(np.linalg.inv(t))




#Name : Satyavan Dhaku Mestry .
#Roll No : 27
#Class: S.Y.Bsc Computer Science
#Linear Algebra using Python Practical  No:07
#7. Write a program to convert a matrix into its row echelon form. 
# import sympy
from sympy import *

M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
print("Matrix : {} ".format(M))

# Use sympy.rref() method
M_rref = M.rref()
	
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))

"""
















