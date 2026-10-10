''' 
=========Max Consecutive Ones
find the max number of times 1 comes continuously in an array
'''

l=[1,0,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1,0,1]
def max1(arr):
    maximum=0
    count=0
    for i in arr:
        if i==1:
            count+=1

        elif i==0:
            maximum=max(maximum,count)
            count=0
    if maximum<count:  # if not included , if the last number is 1 , it will not be added in count
        maximum=count
    return maximum

print(max1(l))
