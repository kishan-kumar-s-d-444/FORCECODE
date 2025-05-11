t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    for i in range(1,n+1):
        cur=0
        for j in range(1,n+1):
            cur+=abs(i-j)
        res+=cur*(n-1)
    if(n==1):
        print(1)
    else:
        print(res)