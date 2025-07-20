t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    rest=False
    day=0
    for i in range(n):
        if(rest):
            rest=False
            continue
        if(a[i]==0):
            day+=1
        else:
            day=0
        if(day==k):
            ans+=1
            day=0
            rest=True
    print(ans)
        