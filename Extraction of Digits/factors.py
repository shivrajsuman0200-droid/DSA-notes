#Brute force

n=int(input("Enter a number: ")) 
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)


# time complexity = O(N)
# space compelexity = O(k)
# where k is the total number of factors(As i can't count all the factors)
#--------------------------------------------------------------

#Better solution 


n=int(input("Enter a number: "))
result=[]
for i in range(1,n//2):
    if n%i==0:
        result.append(i)
result.append(n)
print(result)


# time complexity is O(N/2) which is almost equal to O(N)
# space complexity is O(k)

#--------------------------------------------------------


# Optimal solution
 
from math import sqrt
n=int(input("Enter a number"))
result=[]
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        result.append(i)
        if n//i!=i:
            result.append(n//i)
            
# result.sort()
# print(result)

# timecomplexit => O(N^2)
