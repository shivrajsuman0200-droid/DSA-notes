# Character hashing

# Brute force method


# s="iugsuingsivonjkhagfihoangytbsuifn"
# q=['a','s','f','d']
# for i in q:
#     count=0
#     for j in s:
#         if j==i:
#             count+=1
#         print(count , end=" ")



# time complexity = O(n*m)
# space complexity = O(1) => as the count , i , j all these are always going to be constant
 

# Using Character Hashing

# s="iugsuingsivonjkhagfihoangytbsuifn"
# q=['a','s','f','d']
# d=[0]*26
# for i in range(len(s)):
#     index=ord(s[i])-97
#     d[index]=d[index]+1

# print(d)


# Using dictionary

# s="iugsuingsivonjkhagfihoangytbsuifn"
# q=['a','s','f','d']

# d={}
# for i in range(len(s)):
#     d[s[i]]=d.get(s[i],0)+1
# print(d)


# time complexity = O(n)
# space complexity = O(1)


