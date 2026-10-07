nt(input())
def fibonachi(n,a=1,b=1,count=0):
    if count==n:
        return a
    fibonachi(n,a+=b,b+=a+b,count+=1)
    

     
