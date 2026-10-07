# Print nth fibonachi number

n=int(input())
# def fibonachi(n,a=0,b=1,count=0):
#     if count==n:
#         return a
#     a,b=b,a+b
#     count+=1
#     fibonachi(n,a,b,count)
    


def fibonachi(n):
    if n==1 or n==0:
        return n
    return (fibonachi(n-1) + fibonachi(n-2))    

print(fibonachi(n))
