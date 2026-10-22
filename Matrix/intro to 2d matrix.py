'''
1 2 3
4 5 6
7 8 9
'''

l=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# printing the items of list , as matrix:

# for i in l:
#     for j in i:
#         print(j, end=" ")
#     print()


rows=len(l)
cols=len(l[0])
# for i in range(rows):
#     for j in range(cols):
#         print(l[i][j],end=" ")
#     print()


# --------------printing the upper triangle
for i in range(rows):
    for j in range(cols):
        if i<=j: # here i is rows and j is columns
            # in case of upper triangle i >= j

            print(l[i][j],end=" ")
        else:
            print("*" , end=" ")
    print()

print()
# ----------------------printing the lower triangle
for i in range(rows):
    for j in range(cols):
        if i>=j:
            print(l[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

print()
# ---------------------printing diagonal elements
for i in range(rows):
    for j in range(cols):
        if i==j:
            print(l[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()
#---------------------------- printing the other diagonal elements
for i in range(rows):
    for j in range(cols):
        if j==rows-1-i:
            print(l[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

