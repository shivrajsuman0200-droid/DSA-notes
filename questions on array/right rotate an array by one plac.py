'''right rotate an array by one place '''
def Rightrotation(nums):
    nums[:]=[nums[-1]]+nums[0:len(nums)-1]

l=[1,2,3,4,4,5,6]
# x=Rightrotation(l)
# print(l)


#   without using slicing
def rightRotate(nums):
    temp=nums[-1]
    for i in range(len(nums)-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp

# time complexity => O(n)
# Space complexity => O(1)

# rightRotate(l)
# print(l)

