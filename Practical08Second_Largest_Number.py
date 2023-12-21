#8. Write Python program for finding the second largest element in an array A of size n using 
#Tournament Method. Discuss Time complexity.
def MinMaxArray(Low,High,Second_Largest,arr):
    arr_min=arr[Low]
    arr_max=arr[High]
    arr_Second_Max=arr[Second_Largest]

    #If array has only one element
    if(Low==High):
        arr_min=arr[Low]
        arr_max=arr[Low]
        arr_Second_Max=arr[Low]
        return(arr_min,arr_max,arr_Second_Max)

    #If array hs only two element
    elif(High==Low+1):
        if(arr[Low]>arr[High]):
            arr_min=arr[High]
            arr_max=arr[Low]
            arr_Second_Max=arr_min

 
        else:
            arr_min=arr[Low]
            arr_max=arr[High]
            arr_Second_Max=arr_min
        return(arr_min,arr_max,arr_Second_Max)
    else:
        #There are more than two element in array
        Mid= int((Low+High)/2)
        arr_min1,arr_max1,arr_Second_Max1=MinMaxArray(Low,Mid,Mid-1,arr)
        arr_min2,arr_max2,arr_Second_Max2=MinMaxArray(Mid+1,High,High-1,arr)
        return(min(arr_min1,arr_min2),max(arr_max1,arr_max2),max(arr_Second_Max1,arr_Second_Max2))

#Printing Maximum and Minimum value 
A=[]
R=int(input("Enter number of element in array:"))
for i in range(R):
    a=i+1
    A.append(int(input(f"Enter {a} element in array:")))

print("\nGiven array is:",A)

Low=0#Lower value of array
High=len(A)-1
Second_Largest=len(A)-2

arr_min,arr_max,arr_Second_Max=MinMaxArray(Low,High,Second_Largest,A)
print("\nMinimum element of array is:",arr_min)
print("\nMaximum element of array is:",arr_max)
print("\nSecond maximum element of array is:",arr_Second_Max)



        
