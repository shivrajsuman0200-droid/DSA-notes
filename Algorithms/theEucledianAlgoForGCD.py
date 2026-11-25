'''the Eucleadian algorithm for finding greatest common divisor'''

# Brute force
def gcd(a,b):    # a,b are numbers
    limit = min(a,b)
    for i in range(1,limit+1):
        if a%i==0 and b%i==0 :
            gcd = i


    return gcd ;

# print(gcd(4,8))

# ----------------------------------------------------------------------------------

# Euclidean Algorithm
def EGcf(a,b):
    while b!=0:
        remainder = a%b
        a=b
        b=remainder

    return a

print(EGcf(4,8))
