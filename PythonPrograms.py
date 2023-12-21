
var="hello"
print(type(var))
"""
num1=float(input("Enter a number"))
num2=float(input("Enter 2nd number"))
print(num1+num2)

var=float(input("Enter radius"))
pi=3.14
print("Are of circle is:",pi*(var**2))

age=int(input("Enter a number"))
res=age>18 and age<30
print(res)

num1=10
num2=10
res=num1 is not num2
print(res)

num=int(input("Enter a number"))
res=num>>2
print(res)

a=float(input("Enter a number"))
if(a%2==0):
    print("Even number")
else:
    print("Odd number")
char=input("Enter a charactor")
if(char>='a' and char<='z')or(char>='A' and char<='Z'):
    print(f"{char} is a alphabet")
else:
    print(f"{char}is not an Alphabet")

val=20
val2=40
if(val==20):
    if(val2==40):
        print('Yes')
    else:
        print('No')
else:
    print('No')

s=1
while(s<11):
    print(s)
    s+=1
print('Loop is over')

for i in range(1,11):
    print(i)

s=1
while(s<=20):
    if(s%2!=0):
        print(s)
    s+=1
print("Loop is over")
print("Loop is over")

a=int(input("Enter 1st number"))
b=int(input("Enter 2st number"))
c=int(input("Enter 3rd number"))

if(a>b):
    if(a>c):
        print("Greater number a")
    else:
        print("C is greater ")
elif(b>c):
    print("B is greater")
elif(a==b and a==c):
    print("All are equal")
else:
    print("C is greater")


num=int(input("Enter a number"))
tnum=num
rem=0
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)
if rev==tnum:
    print("palindrome number"

try:
    n1=int(input("Enter 1st number:"))
    n2=int(input("Enter 2nd number:"))
    print(n1+n2)
except ValueError:
    print("====Enter only number....====")



try:
    C1=str(input("Enter 1st character:"))
    C2=str(input("Enter 2nd character:"))
    print(C1+C2)
    n1=int(C1)
    n2=int(C2)
    print(n1+n2)
except ValueError:
    print("")

v
o
r
q
t
print(v)
print(o)
print(r)
print(q)
print(t)

try:
    n1=int(input("Enter 1st number:"))
    n2=int(input("Enter 2nd number:"))
    print(n1/n2)
except ZeroDivisionError:
    print(" Please enter number other than 0 .......")


#Program to print given statement.

Statement=str(input("Enter a statement:"))
print(Statement)
print( "\n The Red Fort or Lal Qila  is a historic fort in Old Delhi,Delhi in India that served as the main residence of the Mughal Emperors. ")


#Declare&print variables
var1="Computer "
var2="science"
print(var1+var2)
var3=int(input("Enter a number:"))
print(var3)
var4=True
print(var4)
print("Data type of var4 is:",type(var4))
var5=complex(input("Enter a complex number:"))
print(var5)
print("Data type if var5 is:",type(var5))
var=var4
print(var)

try:
    var6
    print(var6)
except NameError:
    print("Please Initialize value of var6....")
    

#03)Find sum of numbers
Num1=int(input("Enter first number: "))
Num2=int(input("Enter second number: "))
print(f"Addition of {Num1} and {Num2} is: ",Num1+Num2)
Num3=float(input("Enter a number: "))
print(f"Addition of {Num3} and {Num1+Num2} is:",Num3+(Num1+Num2))

#04)Difference of two numbers
Num1=int(input("Enter first number: "))
Num2=int(input("Enter second number: "))
print(f"Subtraction of {Num1} and {Num2} is: ",Num1-Num2)
Num3=float(input("Enter a number: "))
print(f"Subtraction of {Num3} and {Num1-Num2} is:",Num3-(Num1-Num2))


#04)Multiplication of two numbers
Num1=int(input("Enter first number: "))
Num2=int(input("Enter second number: "))
print(f"Multiplication of {Num1} and {Num2} is: ",Num1*Num2)
Num3=float(input("Enter a number: "))
print(f"Multiplication of {Num3} and {Num1*Num2} is:",Num3*(Num1*Num2))

#06)Division of two numbers
Num1=int(input("Enter 1st number:"))
Num2=int(input("Enter 2nd number:"))
try:

    print(f"Division of {Num1} and {Num2} is: ",Num1/Num2)
except ZeroDivisionError:
    print("  Cannot divide by zero..\n Please re-enter second number....")

#07)Find last digit of number
Num=int(input("Enter a number:"))
rev=0
rem=0
if Num>0:
    rem=Num%10
    print(f"Last digit of {Num} is:",rem)
else:
    print("Please re-enter  number....")
    

#08)Add two digits of a number
Num=int(input("Enter a number: "))
o_Num=Num
digit=0
digit_sum=0
digit_count=0
while Num>0:
    digit=Num%10
    digit_sum +=digit
    digit_count+=1
    if(digit_count==2):
        break
    else:
        Num=Num//10
  
print(f" Addition of last two digits of {o_Num} is: ",digit_sum)


#09)Sum of 3 digits of a number
Num=int(input("Enter a number: "))
o_Num=Num
digit=0
digit_sum=0
digit_count=0
while Num>0:
    digit=Num%10
    digit_sum +=digit
    digit_count+=1
    if(digit_count==3):
        break
    else:
        Num=Num//10

    
print(f" Addition of last three digits of {o_Num} is: ",digit_sum)  

#10)Sum of 4 digits of a number
Num=int(input("Enter a number: "))
o_Num=Num
digit=0
digit_sum=0
digit_count=0
while Num>0:
    digit=Num%10
    digit_sum +=digit
    digit_count+=1
    if(digit_count==4):
        break
    else:
        Num=Num//10

    
print(f" Addition of last four digits of {o_Num} is: ",digit_sum)



#11)Reverse of a 4 digit number
Num=int(input("Enter a number: "))
O_Num=Num
Rev=0
Rem=0
while Num>0:
    Rem=Num%10
    Rev=Rev*10+Rem
    Num//=10
print(f"Reverse of {O_Num} is:",Rev)

#12)Swap using third variable
print("Numbers swapping")
A=int(input("Enter first number:"))
B=int(input("Enter second number:"))
print(f"Before Swapping ,value of A={A} and value of B={B} ")
P=A
A=B
B=P
print(f"After Swapping ,value of A={A} and value of B={B} ")
print("====================================================")

#Character swapping
print("Character swapping")
A=str(input("Enter first Character:"))
B=str(input("Enter second Character:"))
print(f"Before Swapping ,value of A={A} and value of B={B} ")
P=A
A=B
B=P
print(f"After Swapping ,value of A={A} and value of B={B} ")

#13)Swap without third variable
print("Numbers swapping")
A=int(input("Enter first number:"))
B=int(input("Enter second number:"))
print(f"Before Swapping ,value of A={A} and value of B={B} ")
A=A+B
B=A-B
A=A-B
print(f"After Swapping ,value of A={A} and value of B={B} ")


#14)Average of three numbers
Num1=int(input("Enter first number:"))
Num2=int(input("Enter second number:"))
Num3=int(input("Enter third number:"))
Avg=(Num1+Num2+Num3)/3
print(f"The average of {Num1},{Num2} and {Num3} is:{Avg}")


#1. Write Python program to perform matrix multiplication.
#Discuss the complexity of algorithm used.
from numpy import *
Mat1=array([
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ])
Mat2=array([
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ])
Mat3=array([ [0,0,0],
             [0,0,0],
             [0,0,0] ])
print("First Matrix ")
print(Mat1)
print("\n Second Matrix")
print(Mat2)

for i in range(len(Mat1)):
    for j in range(len(Mat2)):
        Mat3 [i][j]=0
        Sum=0
        for k in range(len(Mat2)):
            Sum=Sum+(Mat1[i][k]* Mat2[k][j])
        Mat3[i][j]=Sum

print("\n Multiplication of First and Second matrix")
for R in Mat3:
    print(R)
        


#Program of addition and subtraction of two matrix
from numpy import *
Mat1=array([
            [1,2],
            [3,4]
            ])
Mat2=array([
            [5,6],
            [7,8]
            ])

print("First Matrix")
print(Mat1)
print("\n Second Matrix")
print(Mat2)
print("\n Addition of first and second matrix")
print(Mat1 + Mat2)
print("\n Subtraction of first and second matrix ")
print(Mat1 - Mat2)

#2.Write Python program to sort n names using Quick sort algorithm.
#Discuss the complexity of algorithm used.
# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
	
	# Initializing pivot's index to start
	pivot_index = start
	pivot = array[pivot_index]
	
	# This loop runs till start pointer crosses
	# end pointer, and when it does we swap the
	# pivot with element on end pointer
	while start < end:
		
		# Increment the start pointer till it finds an
		# element greater than pivot
		while start < len(array) and array[start] <= pivot:
			start += 1
			
		# Decrement the end pointer till it finds an
		# element less than pivot
		while array[end] > pivot:
			end -= 1
		
		# If start and end have not crossed each other,
		# swap the numbers on start and end
		if(start < end):
			array[start], array[end] = array[end], array[start]
	
	# Swap pivot element with element on end pointer.
	# This puts pivot on its correct sorted place.
	array[end], array[pivot_index] = array[pivot_index], array[end]
	
	# Returning end pointer to divide the array into 2
	return end
	
# The main function that implements QuickSort
def quick_sort(start, end, array):
	
	if (start < end):
		
		# p is partitioning index, array[p]
		# is at right place
		p = partition(start, end, array)
		
		# Sort elements before partition
		# and after partition
		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)
		
# Driver code
array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')
	
# This code is contributed by Adnan Aliakbar
"""
#2.Write Python program to sort n names using Quick sort algorithm.
# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
#taking user input
#X=[int(input()) for i in range(int(input("How many elements are in list:")))]
#print(X)
X=[]
for i in range(int(input("How many elements are in list:"))):
    print("Enter a name:")
    X.append(str(input()))
    print(X)
def partition(start, end, X):
	
	# Initializing pivot's index to start
	pivot_index = start
	pivot = X[pivot_index]
	
	# This loop runs till start pointer crosses
	# end pointer, and when it does we swap the
	# pivot with element on end pointer
	while start < end:
		
		# Increment the start pointer till it finds an
		# element greater than pivot
		while start < len(X) and X[start] <= pivot:
			start += 1
			
		# Decrement the end pointer till it finds an
		# element less than pivot
		while X[end] > pivot:
			end -= 1
		
		# If start and end have not crossed each other,
		# swap the numbers on start and end
		if(start < end):
			X[start],X[end] = X[end],X[start]
	
	# Swap pivot element with element on end pointer.
	# This puts pivot on its correct sorted place.
	X[end], X[pivot_index] = X[pivot_index],X[end]
	
	# Returning end pointer to divide the array into 2
	return end
	
# The main function that implements QuickSort
def quick_sort(start, end, X):
	
	if (start < end):
		
		# p is partitioning index, array[p]
		# is at right place
		p = partition(start, end,X)
		
		# Sort elements before partition
		# and after partition
		quick_sort(start, p - 1, X)
		quick_sort(p + 1, end, X)
		
# Driver code
#array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(X) - 1,X)

print(f'Sorted array: {X}')
	





























































    
