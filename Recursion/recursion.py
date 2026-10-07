# tail recursion 




# greet()

# head recursion 

n=0
def greet1(n):
    # global n 
    if n==4:
        return
    greet1(n+1)
    print("hello")


greet1(n)