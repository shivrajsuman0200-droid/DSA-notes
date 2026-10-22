'''convert the whole column and row to zero if zero found'''
l=[
    [1,2,6,7,8,0],
    [5,3,6,8,5,2],
    [5,1,4,5,0,4],
    [5,1,1,3,6,8]
]

# brute force method ------------------
cols=len(l[0])
rows=len(l)
row_change=[]
col_change=[]
for i in range(rows):
    for j in range(cols):
        if l[i][j]==0:
            # here i am feeling either i can create a new matrix with changes or i can just store i and j value and later change the same matrix
            # the other option will save storage while the first one will save a little bit time
            # going with the other option 
            row_change.append(i)
            col_change.append(j)
for i in range(rows):
    for j in range(cols):
        if i in row_change or j in col_change :
            l[i][j]=0
        

# for i in l:
#     for j in i:
#         print(j, end=" ")
#     print()

# ---------------------------------------------------------
# instead of appending the values in a separate list , i can also mark that value as infinity and later change that value to 0. BUT I DONT PREFER THIS APPROACH , THE ONE ABOVE WAS BETTER SOLUTION


def mark_infinity(l,row,col):
    for i in range(rows):
        if l[i][col]!=0:
            l[i][col]=float("inf")
    for j in range(cols):
        if l[row][j]!=0:
            l[row][j]=float("inf")

def Convert_inf_to_0(l):
    rows=len(l)
    cols=len(l[0])
    for i in range(rows):
        for j in range(cols):
            if l[i][j]==0:
                mark_infinity(l1,i,j)

    for i in range(rows):
        for j in range(cols):
            if l[i][j]==float("inf"):
                l[i][j]=0

l1=[
    [1,2,6,7,8,0],
    [5,3,6,8,5,2],
    [5,1,4,5,0,4],
    [5,1,1,3,6,8]
]

Convert_inf_to_0(l1)
# for i in l1:
#     for j in i:
#         print(j, end=" ")
#     print()


