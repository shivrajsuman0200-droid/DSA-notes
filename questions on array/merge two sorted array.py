'''Merge two sorted array into one sorted array , but duplicates are not allowed'''

def merge1(l1,l2):
    i,j=0,0
    l3=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:
            if not l3 or l3[-1]!=l1[i]:
                l3.append(l1[i])
            i+=1
        else:
            if not l3 or l3[-1] != l2[j]:
                l3.append(l2[j])
            j+=1

    while j<len(l2):
        if not l3 or l3[-1] != l2[j]:
            l3.append(l2[j])
        j+=1
    while i<len(l1):
        if not l3 or l3[-1]!=l1[i]:
            l3.append(l1[i])
        i+=1      
    return l3



# l1=[1,2,3,4,5,5,6,7,7,8,9,9,99]
# l2=[1,2,3,3,4]
# print(merge1(l1,l2))


# time complexity =  O(n+m)
# space complexity = O(n+m)
