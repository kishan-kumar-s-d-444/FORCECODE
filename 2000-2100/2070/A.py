# i%3==i%5  : 0 1 2 | 15 16 17 | 30 31 32 ... 
t=int(input())
for _ in range(t):
    n=int(input())
    fact=n//15
    last=fact*15
    bound=last+2
    if(bound<=n):
        res=(fact+1)*3
    else:
        res=(fact*3)+(n-last+1)
    print(res)
