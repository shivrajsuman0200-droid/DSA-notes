'''question is to check if the given array is sorted or not'''
#intution is that if a list is sorted , the next number should be greater than the previous one. if it's false break the loop
# and return that list is not sorted
def ifsorted(nums):
    for i in range(len(nums)-1): #cannot run the loop till the end element because in that case i+1 will not exist
        if nums[i]>nums[i+1]:
            return False
    else:
        return True
 


