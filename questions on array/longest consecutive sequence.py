''' Longest Consecutive Sequence

a list is given , you have to find the longest sequence of consecutive numbers
for example [2,1,5,8,100,0,102]

so the output should be (0,1,2) => 3

'''


l=[2,1,5,8,100,0,102,3]
def LCS(l):
    maxi=1
    for i in range(len(l)):
        count=1
        val=l[i]+1
        while val in l:
            val+=1
            count+=1
        maxi=max(count,maxi)
    return maxi

print(LCS(l))


# time complexity = O(n**2)
# space complexity = O(1)



# better solution 

# intution - sort the list and take a last smaller variable

def lcs2(l):
    l.sort()
    last_smaller = float("-inf")
    result=0
    count=1
    for i in l:
        j=i
        if j==last_smaller:
            continue
        elif j-1==last_smaller:
            count+=1
            last_smaller=j
        else:
            count=1
            last_smaller=i
            # print(count)
        result = max(result,count)
    return result
print(lcs2(l))
        
