''' Right Rotate an Array by K Places'''

#brute force
def rotations(nums,k):
    for _ in range(k):
        temp = nums[-1]
        for j in range(len(nums)-2,-1,-1):
            nums[j+1]=nums[j]
        nums[0]=temp


nums = [1,2,3,4,5,6,7,8,9]


#solution 2

def rotations2(nums,k):
    n=len(nums)
    if k>len(nums):
        rotation = k%n
    else:
        rotation = k
    for _ in range(rotation):
        e = nums.pop() #temporary variable
        nums.insert(0,e)
    

# better solution using slicing

def rotatitions3(nums,k):
    index=k
    if k>len(nums):
        index=k%len(nums)
    nums[:]=nums[len(nums)-index:]+nums[:len(nums)-index]

# rotatitions3(nums,905)
# print(nums)
    
# time complexity = O(n)
# space complexity = O(1)




# without slicing


