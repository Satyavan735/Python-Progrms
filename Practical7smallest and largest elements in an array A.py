#7. Write Python program for finding the smallest and largest elements in an array A of size n 
#using Selection algorithm. Discuss Time complexity
from array import *
Array1=array('i',[])
R=int(input("Enter number of element in array:"))
for i in range(R):
    a=i
    Array1.append(int(input(f"Enter {a+1} element of an array:")))
print("\nUnsorted array is:",Array1)

for i in range(len(Array1)):
    min_index=i 
    for j in range(i+1,len(Array1)):
        if Array1[j]<Array1[min_index]:
            min_index=j
    if Array1[i]!=Array1[min_index]:
        Array1[i],Array1[min_index]=Array1[min_index],Array1[i]
print("\nSorted array is:",Array1)
print("\n Smallest element in given array is :",Array1[0])
max_Index=len(Array1)
print("\n Largest element in given array is:",Array1[max_Index-1])
