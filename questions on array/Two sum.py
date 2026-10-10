'''By summing the elements of the list, try to obtain target value

--> Use one element once
--> Only one solution exist
'''

#brute force method

l=[5,9,1,2,4,15,6,3]

def sumFind(l,target):
    indicies=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==target:
                indicies.append(i)
                indicies.append(j)
                return indicies

# print(sumFind(l,10))
                
    
        
# time complexity = O(n(n+1)/2)
# space complexity = O(1)


# we can sacrifice some space for  better time complexity using dictionary
def sumFind2(l,target):
    freq={}
    for i in range(len(l)):
        remaining = target-l[i]
        if remaining in freq:
            return [i,freq[remaining]]
        freq[l[i]]=i

print(sumFind2(l,10))


# time complexity = O(n)
# space complexity = O(n)

        