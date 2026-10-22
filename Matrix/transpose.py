'''taking the transpose of the matrix'''
nums=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
rows=len(nums)
cols=len(nums[0])
result=[[0]*rows for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        result[j][i] = nums[i][j]
print(result)

# time complexity = O(n**2)
# space complexity = O(n)
