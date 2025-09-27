t=int(input())
for _ in range(t):
    n=int(input())
    g=list(map(int,input().split()))
    g.sort()
    n=len(g)
    ans=0
    if(n%2==1):
        ans+=g[0]
    for i in range(n-1,0,-2):
        ans+=g[i]
    
    print(ans)