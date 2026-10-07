nums=[1,1,2,0,7,8,2,3,4,1,6,4,19,20,33,1,11]
for i in range(1,len(nums)):
    j=i-1
    key=nums[i]
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
print(nums)





