# factorial using functional recursion 
'''
5! = 5x4x3x2x1 = 5 x 4!
1! = 1
'''

def factorial(N):
    if N<=1:
        return 1
    return N*factorial(N-1)

# n=int(input("Enter a number"))
# print(factorial(n))

# time complexity = O(N)
# space complexity = O(N)


#factorial using parametric recursion
'''
5! = 5x4x3x2x1
'''
def factorialP(N,output=1):
    if N<=1:
        print(output)
        return
    output*=N
    factorialP(N-1,output)


N=int(input())   
factorialP(N)

