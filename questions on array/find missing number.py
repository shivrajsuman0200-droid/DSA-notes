'''Find Missing Number in an Array'''
l=[1,2,3,4,5,7] #6

# ==================Brute force method

def missing(nums):
    x=len(nums)
    for i in range(1,x+1):
        if i not in nums:
            return i

# print(missing(l))

# time complexity = O(n*n)
# space complexity = O(1)


# ====================Better solution => using dictionary

def missing2(nums):
    # creating a dictionary
    freq={}
    for i in range(1,len(nums)+1): 
        freq[i]=0
    # adding frequency in it
    for i in nums:
        freq[i]=1
    #finding the missing number
    for i,j in freq.items():
        if j==0:
            return i

# print(missing2(l))


#   ========================================= optimal solution

def missingNum(nums):
    n=len(nums)+1
    return (n*(n+1))//2-sum(nums)

print(missingNum(l))
        
