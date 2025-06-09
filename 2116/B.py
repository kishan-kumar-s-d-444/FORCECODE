MOD=998244353
t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    res=[]
    for i in range(n):
        temp=0
        for j in range(i+1):
            temp=max(temp,(2**p[j]+2**q[i-j])%MOD)
        res.append(temp)
    for it in res:
        print(it,end=" ")
    print("\n")