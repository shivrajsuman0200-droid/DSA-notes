'''Best Time to Buy and Sell Stock'''
'''
there is a list 
[1,2,3,4,2,10,7,13,9,2,5,1]
the prices of stock keeps changing each day , each element of the list is the
price of stock on that day.

rules are simple
1)you can buy stock any time in the list
2)you can sell on any day after buying, but not on the same day.
3)if there is no profit possible return 0
4)else return maximum profit possible'''


# Brute force solution 
l=[1,2,3,4,2,10,7,13,9,2,5,1]
def stock_profit(l):
    maximum_profit=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]-l[i]>maximum_profit:
                maximum_profit=l[j]-l[i]
    if maximum_profit<0:
        return 0
    else:
        return maximum_profit 
print(stock_profit(l))
# time complexity = O(n**2)
# space complexity = O(1)


# optimal solution
'''intitution is that we will keep a note of the one that comes first(in this case minimum value) and keep checking the final outcome (in this case it's profit).'''
def stock_profit_1(l):
    min_value=float("inf")
    max_profit=0
    for i in l:
        min_value=min(min_value,i)
        max_profit=max(max_profit,i-min_value)
    return max_profit

print(stock_profit_1(l))

# time complexity = O(n)
# space complexity = O(1)