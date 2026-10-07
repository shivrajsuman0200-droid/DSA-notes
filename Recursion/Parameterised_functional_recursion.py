# Difference between parameterised and functional recursion 


# Sum of 1 to N (parameterised recursion)

# def sum(n,i,s):
#     if i>n:
#         print(s)
#         return
#     print(s)
#     sum(n,(i+1),(s+i))

# sum(4,1,0)


# Sum of 1 to N (Functional recursion)

def func(N):
    if N==1:
        return 1
    return N+ func(N-1)

print(func(10))