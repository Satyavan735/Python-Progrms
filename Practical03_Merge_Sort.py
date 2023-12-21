#3. Write Python program to sort n numbers using Merge sort algorithm. Discuss the complexity 
#of algorithm used.


#Divide the list into sublist untile it contain single element
def Merge_Sort(List):
    if len(List)>1:#Base condition if list contain single element the stop divide
        mid=len(List)//2
        Left_li=List[:mid]
        Right_li=List[mid:]
        Merge_Sort(Left_li)
        Merge_Sort(Right_li)

        i=0 #index of left list
        j=0 # index of right list
        k=0 #index of original list
        #For comparing and Merge value
        while i<len(Left_li)and j<len(Right_li):
            if Left_li[i]<Right_li[j]:
                List[k]=Left_li[i]
                i=i+1  # for checking next value
                k=k+1  #for adding value to the next position
            else:
                List[k]=Right_li[j]#Right List value will be smaller
                j=j+1
                k=k+1
         #For Merge value which is left
        while i<len(Left_li):
            List[k]=Left_li[i]
            i=i+1
            k=k+1
        while j<len(Right_li):
            List[k]=Right_li[j]
            j=j+1
            k=k+1

#Calling function
Range=int(input("Enter number of element you want in list:"))
List=[]
for i in range(Range):
    List.append(int(input("Enter an element in list:")))
print("\n List before sorting in ascending order:",List)
Merge_Sort(List)
print("\n List after sorting in ascending order:",List)
    
        
        
    
