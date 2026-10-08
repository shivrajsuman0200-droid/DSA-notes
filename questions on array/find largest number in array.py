# finding largest element in array 

# let's try this on my own first 
nums = [-22,1,100,819,2,-1000,3,0.1,39]
def largest_01(nums):
    largest=nums[0] # assuming the first element as the largest element
    for i in nums:
        if i>largest:
            largest=i
    return (f"largest number is: {largest}")

'''time complexity => O(n)
space complexity => O(1)
'''

def largest_02(nums):
    largest=float("-inf") # taking negative infinity as the initial value of largest element
    for i in nums:
        largest = max(largest,i) #skipping the if statement 
    return largest
        
