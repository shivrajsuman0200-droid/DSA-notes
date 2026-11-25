'''1234
will return 1+2+3+4 = 10
1+0 = 1
so 1 should be the answer'''

n = int(input())
while n>=10:
    total=0
    while n>0:
        total += n%10
        n//=10
    n=total
print(n)

