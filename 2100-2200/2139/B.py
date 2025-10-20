t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    for i in range(n-1,-1,-1):
        ans+=(a[i]*m)
        m-=1
        if(m<=0):
            break
    #dsada
    print(ans)

