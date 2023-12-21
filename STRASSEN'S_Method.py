#10. Write Python program for implementing Strassen's Matrix multiplication using Divide and 
#Conquer method. Discuss the complexity of algorithm.
#STRASSEN'S Method for multiplication of two matrix
import numpy as np
#First Matrix Value
print("Enter first matrix value:\n")
a=int(input("Enter 1st number:"))
b=int(input("Enter 2st number:"))
c=int(input("Enter 3st number:"))
d=int(input("Enter 4st number:"))

#Second Matrix Value
print("\n Enter second matrix value:")
e=int(input("Enter 1st number:"))
f=int(input("Enter 2st number:"))
g=int(input("Enter 3st number:"))
h=int(input("Enter 4st number:"))

#Print first matrix
R1=[]
R2=[]
R1.append(a)
R1.append(b)
R2.append(c)
R2.append(d)
m1=[]
m1.append(R1)
m1.append(R2)
Mat1=np.matrix(m1)
print("\nFirst matrix is:")
print(Mat1)

#Print second matrix
r1=[]
r2=[]
r1.append(e)
r1.append(f)
r2.append(g)
r2.append(h)
m2=[]
m2.append(r1)
m2.append(r2)
Mat2=np.matrix(m2)
print("\nSecond matrix is:")
print(Mat2)

#Multiplication of matrix
p1=a*(f-h)
p2=(a+b)*h
p3=(c+d)*e
p4=d*(g-e)
p5=(a+d)*(e+h)
p6=(b-d)*(g+h)
p7=(a-c)*(e+f)

A=p5+p4-p2+p6
B=p1+p2
C=p3+p4
D=p1+p5-p3-p7

#Printing Matrix
row1=[]
row1.append(A)
row1.append(B)

row2=[]
row2.append(C)
row2.append(D)

Mat3=[]
Mat3.append(row1)
Mat3.append(row2)

M3=np.matrix(Mat3)
print("\nMultiplication of first and second matrix is:")
print(M3)

