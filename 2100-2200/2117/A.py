t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    start,end=float('inf'),float('-inf')
    for i in range(n):
        if(a[i]==1):
            start=min(start,i)
            end=max(end,i)
    if(end-start+1<=x):
        print("YES")
    else:
        print("NO")