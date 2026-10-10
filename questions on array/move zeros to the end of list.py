'''Move Zeros to the End of the List without creating a new list '''


list1 = [1, 2, 3, 4, 0,0,0,0,0,5, 6, 0, 0, 9, 0, 8]
def moveZero(nums):
    i = 0
    count = 0

    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            # i+=1 (adding i+=1 here misses consecutive zeros and not adding it creates and infinite loop)
            # therefore using two variables
            nums.append(0)
        else:
            i += 1
        count += 1

# moveZero(list1)
# print(list1) 


# optimal solution 

def moveZero1(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
 
'''here i  marks the non zero element and keep increasing on every iteration
while j start with i in the loop but stops when nums[i]==0 , i continues to move ahead while j stays there 
and on the very next itteration when i finds a non zero number , they swap. J only moves ahead when swapping happens   '''

# moveZero1(list1)
# print(list1)

# time complexity = O(n)
# space complexity = O(1)
