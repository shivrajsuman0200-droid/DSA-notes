'''Maximum Subarray Sum - Kadane's Algorithm

find the subarray whose sum will be maximum
and return the maximum value'''

l=[1,2,3,-2,-3,-10,10,2,1,0,-3,2,-20,0,10,1]
def maximum_subArray_sum(l):
    maxi=float("-inf")
    sum=0
    for i in range(len(l)):
        for j in range(i,len(l)):
            sum=sum+l[j]
            maxi=max(maxi,sum)
        sum=0
    return maxi

print(maximum_subArray_sum(l))

# time complexity = O(n**2)
# space complexity = O(1)


# optimal solution
'''here intution is whenever the count will become negative i will stop adding and will start counting further from 0.(count get's reset whenever count's value gets less than)'''
def maximum_subarray_sum2(l):
    maxi=float("-inf")
    count=0
    for i in range(len(l)):
        count+=l[i]
        maxi=max(maxi,count)
        if l[i]<0:
            count=0
    return maxi

print(maximum_subarray_sum2(l))



# time complexity = O(n)
# space complexity = O(1)

