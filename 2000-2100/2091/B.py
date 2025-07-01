t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    tot=0
    s=n
    b=float('inf')
    for i in range(n-1,-1,-1):
        v1=s-i
        v2=min(b,a[i])
        if(v1*v2>=x):
            tot+=1
            s=i
            v2=float('inf')
    print(tot)

