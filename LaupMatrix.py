# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:46:54 2022

@author: Administrator


#import numpy as np
#print("Print Matrix using array")
#A=np.array([[1,2,2],[2,3,4]])
#print(A)
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


vm=[]
for i in range(r):
    for j in range(c):
            vm.append(Mat[j][i])
    print()

print(vm)

Sum=0
for i in range(len(T)):
    for j in range(len(vm)):
        Sum=Sum+(T[i]*vm[j])
    
print(Sum)
                   
  """
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
          

