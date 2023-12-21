#1. Write Python program to perform matrix multiplication. Discuss the complexity of algorithm 
#used
"""
from numpy import *

Matrix1=array([[5,6,3],
                [7,9,6],
                [8,10,3]
                ])
Matrix2=array([[6,4,6],
                [2,3,7],
                [1,4,11]
                ])
Matrix3=array([[0,0,0],
               [0,0,0],
                [0,0,0]
                ])
print("\n Printing Matrix1:")
print(Matrix1)
print("\n Printing Matrix2:")
print(Matrix2)  
for i in range(len(Matrix1)):
    for j in range(len(Matrix2)):
        Matrix3[i][j]=0
        Sum=0
        for k in range(len(Matrix2)):
            Sum=Sum+(Matrix1[i][k]*Matrix2[k][j])
        Matrix3[i][j]=Sum
print("\n Multiplication of Matrix1 and Matrix2 is:")
for R in Matrix3:
    print(R)                           
"""

# Program to multiply two matrices using nested loops
import numpy as np

X = []
R=int(input("Enter number column in matrix:"))
C=int(input("\n Enter number of rows in matrix:"))
for i in range(R):
    A=[]
    for j in range(C):
        A.append(int(input("Enter element of first matrix:")))
    X.append(A)
print("\nFirst Matrix is:")
print(np.matrix(X))


Y = []
R1=int(input("Enter number column in matrix:"))
C1=int(input("\n Enter number of rows in matrix:"))
for i in range(R1):
    A1=[]
    for j in range(C1):
        A1.append(int(input("Enter element:")))
    Y.append(A1)
print("\n2nd  MAtrix is:")
print(np.matrix(Y))


result = []

for i in range(R1):
    A2=[]
    for j in range(C1):
        A2.append(int(0))
    result.append(A2)
print("\n3rd  MAtrix is:")
print(np.matrix(result))


# iterate through rows of X
for i in range(C):
   # iterate through columns of Y
   for j in range(R1):
       # iterate through rows of Y
       for k in range(C1):
           result[i][j] += X[i][k] * Y[k][j]

print("\n Matrix Multiplication")
print(np.matrix(result))






































