t=int(input())
for _ in range(t):
    n=int(input())
    res=[-1]*(n)
    flag=True
    ind=1
    for i in range(n):
        if(res[i]==-1):
            res[i]=ind
            ind+=1
        if(res[n-i-1]==-1):
            res[n-i-1]=ind
            ind+=1
    for it in res:
        print(it,end=" ")
    print("\n")