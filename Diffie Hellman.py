#Diffie Hellman Algorithm 
import Prime_Number as np
#Prime number input
def PrimeInput():
    G=int(input("Enter a prime number: "))
    Flag=np.PrimeNumber(G)
    if Flag!=1:
        g=PrimeInput()
        return g
    else:
        return G
g=PrimeInput()
#print(g)
#Natural number greater than 1
def NaturalNumber():
    N=int(input("Enter any natural number other than 0 and 1: "))
    if N<=1:
        print("=======Please enter number greater than 1 ====== ")
        n=NaturalNumber()
        return n
    else:
        return N
Num=NaturalNumber()
#print(Num)
#Calculate Remainder
Rem=g%Num

print(Rem)
#Prime Series Function
PrimeSeries=[]#Prime series list up to x
def Prime_Series(X):
    for i in range(X+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                PrimeSeries.append(i) 
Prime_Series(Rem)    
print("Prime series :",PrimeSeries)

X=0
Y=0
#Function to get values of X and Y
def CalculateKeys(PrimeLi,R,F):
    if F==1:
        RemIndex=PrimeLi.index(R)
        x=PrimeLi[RemIndex-1]
        y=PrimeLi[RemIndex-1]
        if x==y:
            print("X is equal to Y is: ",x==y)
            return x,y
        else:
            print("X is equal to Y is: ",x==y)
    else:
        x=max(PrimeLi)
        y=max(PrimeLi)
        return x,y

#Call
if Rem>=3:
    F=np.PrimeNumber(Rem)
    X,Y=CalculateKeys(PrimeSeries,Rem,F)
    print(f"Value of X is: {X} and Value of Y is: {Y}")
else:
    print("Operation failed !!.....")

#Calculate A and B
A=(g**X)%Num
B=(g**Y)%Num
#A=(g**3)%Num
#B=(g**5)%Num
print(f"Value of A is: {A} and Value of B is: {B}")

#Calculate KA and KB7
KA=(B**X)%Num
KB=(A**Y)%Num
#KA=(B**3)%Num
#KB=(A**5)%Num
print(f"Value of KA is: {KA} and Value of KB is: {KB}")

if KA==KB:
    print("KA and KB both are equal...")
    print(f"Respective key values are :X={X} and Y={Y}")