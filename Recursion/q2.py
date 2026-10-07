#video number 16
# complete reversal of the array
array=[5,7,3,2,6,1,5,9]
def reverse(arr,count=0):
    if count==len(arr):
        return
    reverse(arr,count+1)
    print(arr[count],end=" ")
# reverse(array)

# time complexity = O(n)
# space complexity = O(n) =>stack space
#-----------------------------------------------------------------------------------------------

# method 2 => better approach because this can reverse the function from anywhere we want

def reverse2(arr,l,r):
    if l>=r:
        return (arr)
    arr[l],arr[r]=arr[r],arr[l]
    reverse2(arr,l+1,r-1)

reverse2(array,2,5) #reversing the list inbetween index 2 to index 5
print(array)

# time complexity= O(n/2) -- O(n)
# space complexity = O(n/2) -- O(n)  => stack space
#-----------------------------------------------------------------------------------------------


# Using while loop 

def reverse3(arr,l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

# reverse3(array,2,5)
# print(array)
