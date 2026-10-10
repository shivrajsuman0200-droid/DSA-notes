'''rearrange the elements by sign

a list will be given , while keeping the order same
you have to arrange the list in +-+-+-+- format. '''


# brute force method
l=[5,10,-3,-10,-1,6]
def rearrange(l):
    lp=[]
    ln=[]

    for i in range(len(l)):
        if l[i]<0:
            ln.append(l[i])
        elif l[i]>=0:
            lp.append(l[i])
    for i in range(len(ln)):
        l[2*i]=lp[i]
        l[2*i+1]=ln[i]
    return l

print(rearrange(l))
# time complexity = O(n+n/2)
# space complexity = O(n)


# Optimal solution

def rearrange2(l):
    result=[0]*len(l)
    a,b=0,1  # a is positive index and b is negative index
    for i in l:
        if i>=0:
            result[a]=i
            a+=2
        else:
            result[b]=i
            b+=2
    return result

print(rearrange2(l))





        
        



    
        
        