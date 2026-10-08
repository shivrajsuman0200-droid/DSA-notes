'''linear search , find the first occurrence of the target element and return it's index, if not found return -1  '''



def linearSearch(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1

        
list1 = [1, 2, 3, 4, 0,0,0,0,0,5, 6, 0, 0, 9, 0, 8] 
print(linearSearch(list1,10))