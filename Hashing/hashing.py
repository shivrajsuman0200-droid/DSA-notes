# prestoring some values into some data structure line List/Dictionary/Sets 
# and fetching it 

#Brute force                            # constraints :-
#n=[5,4,3,2,4,4,4,4,5,5,5,7,5,3,4,3,4,10]      #1<=n[i]<=10
#m=[4,33,22,5,34,6,8,5,3,2,1,10,2,5,5]   # n,m can have 10^8 elements
# for num in m:
#     count=0
#     for i in n:
#         if num==i:
#             count+=1
# print(count)

# timecomplexity = O(m*n)
# space complexity = O(1)


# worst case will be 
# where n contains 10^8 elements and m contains 10^8 elements too = 10^16 (which is greater than 10^8)
# in that case the time , this will exceed the time limit 
# and will through TLE (time limit exceeded) error


#Method 2
# Using a predefined list 


# hash_list=[0]*11
# for i in n:
#     hash_list[i]+=1
# # print(hash_list)
    
# for i in m:
#     if i>=10 or i<0:
#         print(0 , end=" ")
#     else:
#         print(hash_list[i] , end=" ")

# time complexity = O(n+m)
# space complexity = O(1)

#===============================================================================================

# Using dictionary 
n=[5,4,3,2,4,4,4,4,5,5,5,7,5,3,4,3,4,10]
m=[4,33,22,5,34,6,8,5,3,2,1,10,2,5,5]
hash_map= dict()
for i in range(0,len(n)):
    hash_map[(n[i])]=hash_map.get(n[i],0)+1  
print(hash_map)

for i in m:
    if i in hash_map:
        print(hash_map[i] , end=" ")
    else:
        print(0,end=" ")



# time complexity = O(n+m)
# space complexity = O(n) 
# this code will work even if we remove the constraint ( 0<n<=10)