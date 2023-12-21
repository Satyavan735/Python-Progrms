#RSA Algorithm Program
#Program to find prime number
Plain_Text=int(input("Enter plain text:"))
p=0
q=0
#Function to take only prime number as input
def PrimeNoInput():
    p=int(input("Enter value of P:"))
    q=int(input("Enter value of q"))
    return p,q
p,q=PrimeNoInput()
Flag=0
#Function to check whether a given number is prime or not.
def PrimeNumber(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                print(n,"is not a prime number")
                break
        else:
            print(n,"is prime number")
            Flag=1
            return Flag
    else:
        print(n,"num is not a prime number")
#Function to calculate N  
def Caluculate_N(p,q):
    First_Prime=PrimeNumber(p)
    Second_Prime=PrimeNumber(q)
    if First_Prime==1 and Second_Prime==1:
        N=p*q
        print(N)
        pn=p
        qn=q
        return N,pn,qn
    else:
        print("Please enter only prime number for key")
        p,q=PrimeNoInput()
        N,pn,qn=Caluculate_N(p,q)
        return N,pn,qn
N,pn,qn=Caluculate_N(p,q)
#print(p,"",q,"",N)
#Function to calculate Public key
PublicKey=0
def Next_Prime(Max_F):
    if Max_F==2:#Because 2 is only even prime
        PublicKey=3
        return PublicKey
    else:
        i=2
        while i>1:
            Next_Max=Max_F+i
            for j in range(2,Next_Max):
                if(Next_Max%i==0):
                    print(Next_Max,"is not a prime number")
                    break
            else:
                PublicKey=Next_Max
                return PublicKey
                break
            i+=2    
        
print(pn,"",qn)
x=(pn-1)*(qn-1)
print("X =",x)
Factor_li=[]#Factor list 
PrimeSeries=[]#Prime series list up to x
def Prime_Series(X):
    for i in range(X+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                PrimeSeries.append(i) 
Prime_Series(x)    
print("Prime series :",PrimeSeries)

#Find prime factors of x
def Factors(X,PrimeSeries):
    for i in range(len(PrimeSeries)):
        if X%PrimeSeries[i]==0:
            div=X//PrimeSeries[i]
            Factor_li.append(PrimeSeries[i])
            if div>1:
                Factors(div,PrimeSeries)
                break
        
             
Factors(x,PrimeSeries)
print("Factor list:",Factor_li)            
Max_Factor=max(Factor_li)
print("Max factor:",Max_Factor)
#Calling Next_Prime function for public key
PublicKey=Next_Prime(Max_Factor)
    
print("Public Key:",PublicKey)
#Private key
#Formula=(PrivateKey*PublicKey)mod(p-1)(q-1)=1
i=1
while i>0:
    if (i*PublicKey)%(x)==1: #When public key 3 private key 7
        PrivateKey=i
        break
    i+=1
print("Private Key:",PrivateKey)

print("N =",N)
#Cipher Text Formula:(PlainText**Public key)mod N
Cipher_Text=(Plain_Text**PublicKey)%N
#Cipher_Text=(7**3)%33
print("Encrypted Text:",Cipher_Text)

#Decryption algorithm
#Plain Text Formula:(Cipher Text**Private Key)mod N
PlainText=(Cipher_Text**PrivateKey)%N
print("Decrypted Text:",PlainText)





