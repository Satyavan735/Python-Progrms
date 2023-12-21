# Python3 program to find modular
# inverse of a under modulo m

# A naive method to find modulor
# multiplicative inverse of 'a'
# under modulo 'm'

  #GCD calculation program
def GCD(a,b):
    if a>b:
        if b!=0:
            if a % b==0:
                print(f"\n GCD of{a} and {b} is: ",b)
                return b
            else:
                r=a % b
                g=GCD(b,r)
                return g
        else:
            print("\n Second number must be greater than zero..")
    
            

def modInverse(A, m):
	
	for x in range(1, m):
		if (((A%m) * (x%m)) % m == 1):
			return x
	return -1


# Driver Code
A = 4
m = 26
gcd=GCD(44,m)
print(gcd)
# Function call
print(modInverse(A, m))

# This code is contributed by Nikita Tiwari.
