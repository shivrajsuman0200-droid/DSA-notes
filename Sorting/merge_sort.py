'''
merge sort consists of two functions , the first one recursively divides the array till the number of element reaches 1 , the second fuction merges the two sorted array (pay attention to the word sorted) and trick here is , if the array consists only 1 element it is already sorted
'''

#merging two sorted arrays
def merge_array(arr1,arr2):
    result=[]
    n=len(arr1)
    m=len(arr2)
    i,j=0,0 
    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    if i<n:
        while i<n:
            result.append(arr1[i])
            i+=1
    if j<m:
        while j<m:
            result.append(arr2[j])
            j+=1
    return result


def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = mergeSort(left_arr)
    right = mergeSort(right_arr)
    return merge_array(left,right)

l=[1,2,3,9,8,7,6,1,2,6,4]
print(mergeSort(l))

