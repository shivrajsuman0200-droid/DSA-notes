'''
quick sort works on 2 points 
1) pick a pivot <you can pick any number as pivot>
2) put that pivot at it's right place 
'''

#putting pivot at it's right place
'''
let nums = [4,3,2,1,5,6,9]
we will take two points one is high(H) and one low (L)
take low one in pivot variable
keep moving i form low towards   right side | search for number larger than the pivot
keep moving j from high towards left | search for number smaller than the pivot 
and then swap both
once i and j crosses 
swap the pivot with j
'''

def partition(nums,low,high):
    pivot = nums[low]
    i,j=low,high
    while i<j :
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>=pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j


'''few doubts :
---------------
Q.why i<=high-1 => because the inner loop doesnt care about the coditions of outer loop, to stop it from crossing the   high value we use i<=high-1 | similarly with j>=low+1.
Q.why not i<=high , why high-1 => because the the last value is reserved for high , similarly starting value is reserved for low. 
'''

# quick sort 
def quick_sort(nums,low,high):
    if low<high:
        partition_index = partition(nums,low,high)
        quick_sort(nums,low,partition_index-1)
        quick_sort(nums,partition_index+1,high)



nums = [1,2,9,8,4,0,5,6,3,2]
quick_sort(nums,0,len(nums)-1)
print(nums)