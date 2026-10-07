num=[2,3,12,4,2,1,3,5,6,3,2,2,4,3,1,3,45,2,4,6,7,5,4,2,1,4]

# Brute force 

# freq_map=dict()
# for i in range(0,len(num)):
#     if num[i]  in freq_map:
#         # freq_map[i]=(freq_map[i])+1 =>wrong
#         freq_map[num[i]]+=1
#     else:
#         freq_map[i]=1

# print(freq_map)

# timecomplexity is O(N)
# --------------------------------------------------------


# better method

hash_map={}
n=len(num)
for i in range(0,n):
    hash_map[num[i]]=hash_map.get(num[i],0)+1 # get serches the dictionary for num[i] , when not found it returns the next value which is 0.
print(hash_map)
