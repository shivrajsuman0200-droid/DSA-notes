'''Rotating a matrix by 90 degrees'''

l=[
    [1,2,3,4],
    [5,6,7,8],
    [9,11,12,13],
    [14,66,3,11],
    [0,0,2,3]
]

result=[[0]*len(l) for _ in range(len(l[0]))]
for i in range(len(l)):
    for j in range(len(l[0])):
        result[j][i]=l[i][j]

for i in result:
    for j in i:
        print(j,end=" ")
    print()
        