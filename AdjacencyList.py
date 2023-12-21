"""
m=[]
r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))
#for user input
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    m.append(a)
#Printing matrix
for i in range(r):
    for j in range(c):
        print(m[i][j],end=" ")
    print()

#print adjacency list
def adj_list(m):
    for i in range(r):
        for j in range(c):
            if m[i][j]==1:
                print(f"{i}-->{j}"," ")
        print()
print(adj_list(m))
"""
#Program to print Adjacency Matrix ,Adjacency List,Indegree and Outdegree
#Take Matrix input from user
import numpy as np
ADJ_Matrix=[]
M_Row=int(input("Enter the number of rows:"))
M_Column=int(input("Enter the number of columns:"))
print("\nEnter the rowwise entries:")

#For user inputs
print("Edge represented by 1,Otherwise enter 0 ")
for i in range(M_Row): #A for loop for row entries
    X=[]
    for j in range(M_Column): #A for loop for column entries
        X.append(int(input("Enter element:")))
    ADJ_Matrix.append(X)

print("\n Adjacency matrix:")    
#Print Matrix
for i in range(M_Row):
    for j in range(M_Column):
        print(ADJ_Matrix[i][j],end=" ")
    print()

def ADJ_LIST(ADJ_Matrix):
    for i in range(M_Row):
        C=1
        for j in range(M_Column):
            if ADJ_Matrix[i][j]==1:
                print(f"{i}-->{j}",end=" ")
        print()
        
print(ADJ_LIST(ADJ_Matrix))

degree=0
def degree(vertex):
    for i in range(ADJ_Matrix[vertex]):
        for j in range(ADJ_Matrix):
            if ADJ_Matrix[i][j]==1:
                degree+=1
            
            
                
            
        

degree(0)






























