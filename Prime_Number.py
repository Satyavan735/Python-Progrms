#Prime_Number File
Flag=0
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


