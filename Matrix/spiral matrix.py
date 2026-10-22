'''
printing a matrix in spiral manner : 
'''

l=[
    [1,2,3,4,5,6],
    [20,21,22,23,24,7],
    [19,32,33,34,25,8],
    [18,31,36,35,26,9],
    [17,30,29,28,27,10],
    [16,15,14,13,12,11]
]

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    result=[]

    # initialising pointers for traversal
    top,left=0,0
    bottom,right=len(matrix)-1,len(matrix[0])-1 
    # bottom is no of rows - 1 
    # top is no of columns - 1

    # Traverse the matrix in spiral order :
    while top <=bottom and left<=right:

        # move left to right across the top row
        for i in range(left,right):
            result.append(matrix[top][i])     # why are we using matrix[top]? => we are using matrix[rows][columns] pattern , here top denotes rows while columns are denoted by columns
        top+=1

        # move from top to bottom along the last column 
        for i in range(top,bottom):
            result.append(matrix[i][right]) # same reason here , right is the fixed columns here while the rows are changing and denoted by i here.
        right-=1

        # move from right to left across bottom row
        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1

        # move from bottom to top along the left column
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[bottom][i])
            left+=1


    