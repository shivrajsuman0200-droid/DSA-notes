nums=[1,2,1,2,0,7,8,2,3,4,1,6,4,19,20,33,1,11]
def selection_sort(nums):
    n=len(nums)
    for i in range(0,n): 
        j=i 
        least_index=i
        while j<n: 
            if nums[least_index]>nums[j]:  
                least_index=j   
            j+=1                
        nums[i],nums[least_index]=nums[least_index],nums[i] 
    return nums

print(selection_sort(nums))

# time complexity =  O(n(n+1)/2 almost equal to O(n*n)
# space complexity = O(1)


            



