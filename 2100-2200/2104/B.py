t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    pre=[0]*(n)
    maxi=0
    for i in range(n):
        maxi=max(maxi,a[i])
        pre[i]=maxi
    suf=[0]*(n)
    sm=0
    for i in range(n-1,-1,-1):
        sm+=a[i]
        suf[i]=sm    
    res=[0]*(n)

    for i in range(n-1,-1,-1):
        if(i==n-1):
            res[i]=pre[i]
        else:
            res[i]=suf[i+1]+pre[i]
    
    for i in range(n-1,-1,-1):
        print(res[i],end=" ")
    print("\n")
        