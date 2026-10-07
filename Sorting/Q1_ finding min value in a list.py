# finding the minimum value 
#WILL BE USED IN SELECTION SORT
l=[1,2,0,7,8,2,3,4,1,6,4,19,20,33,1,11]
i=0
min_value=l[0]
while i<len(l):
    if l[i]>=min_value:
        i+=1
    else:
        min_value=l[i]
        # print(min_value)??
        i+=1
print(min_value)

    
    
