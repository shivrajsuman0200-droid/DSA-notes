'''Remove Duplicates from a Sorted Array
the question wants you to bring the unique elements towards left in the array itself
and tell the number of unique elements
'''

# best way is to use a dictionary to find unique value . later use dictionary to update the array


def remDup(nums):
    freq_map = {}
    for i in nums:
        freq_map[i]=0
    j=0
    for k in freq_map:
        nums[j]=k
        j+=1 #number of unique elements
    return j

nums=[1,1,1,2,2,2,3,3,4,5,6,7,7,7,8,8,8,9]
# time complexity = O(2N) = O(N)
# space complexity = O(2N) = O(N)
        
def optimalSoln(nums):
    if len(nums)==1:
        return 1
    else:
        i,j=0,i+1
        while i<len(nums)-1 and j<len(nums):
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i] 
            j+=1
        return i+1 # number of unique elements
    
# time complexity = O(n)
# space complexity = O(1)


# Optimal solution 

def reverse(nums,left,right):
    while left >right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right+=1
n=len(nums)
k=int(input())
reverse(n-k,n-1) # reverse last k elements
reverse(0,n-k-1) # reverse remaining elements
reverse(0,n-1) # reverse whole array

# timecomplexity = O(n)
# space complexity = O(1)



        
