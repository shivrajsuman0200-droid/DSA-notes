nums=[1,2,1,2,0,7,8,2,3,4,1,6,4,19,20,33,1,11]
def bubbleSort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j] 
                is_swap=True
        if is_swap==False:
            return nums
    return nums
    

            
      
print(bubbleSort(nums))




# time complexity = O(n(n+1)/2) => O(n**2)  => in worst and avg case
# space complexity = O(1)
