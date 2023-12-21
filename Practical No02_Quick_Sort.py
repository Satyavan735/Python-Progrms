#2. Write Python program to sort n names using Quick sort algorithm. Discuss the complexity of 
#algorithm used

#Function toget correct position of pivot elemet
def Pivot_Position(List,First,Last):
    Pivot=List[First]
    left=First+1
    right=Last
    while True:
        while left<=right and List[left]<=Pivot:
            left=left+1
        while left<=right and List[right]>=Pivot:
            right=right-1
        if right<left:
            break
        else:
            List[left],List[right]=List[right],List[left]
    List[First],List[right]=List[right],List[First]
    return right

def Quick_Sort(List,First,Last):#Dividing the list according to pivot element
    if First<Last:#Bas case = First==Last ,Partition of list,When list contain single element the stop everything 
        pivot=Pivot_Position(List,First,Last)
        Quick_Sort(List,First,pivot-1)
        Quick_Sort(List,pivot+1,Last)

    #Function not returning any value because we didnot create new list just sorting original list
#Calling the functions
Range=int(input("Enter the range of list"))
List=[]
for i in range(Range):
    List.append(int(input("Enter an element in list:")))
print("List before sorting in ascending order :",List)
length=len(List)
Quick_Sort(List,0,length-1)
print("List after sorting in ascending order :",List)
