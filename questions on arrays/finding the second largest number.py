'''Find the Second Largest Element in an Array Without Sorting'''

#---------------------trying on my own----------------------------------->
'''one way i can think of is to find the largest element then remove it and then find the largest again (this will be 2nd largest)'''
#or better way is ,  i take 2 variables , keep on searching the larger values , once i find any larger value , i will store the previous value of largest variable into sec_largest variable before updating the value of largest variable.


def sec_largest(nums):
    second_largest = float("-inf")
    largest = float("-inf")
    for i in nums:
        if i>largest:
            sec_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
    return(sec_largest)

l=[1,2,3,9,1,10,1000,2000,30,4,-92,-900,0]
# print(sec_largest(l))

# time complexity = O(n)
#space complexity = O(1)