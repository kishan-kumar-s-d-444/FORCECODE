t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    res=[]
    for i in range(n):
        res[i]=a[i]+(a[i]%(k+1))*k
    n=len(res)
    for i in range(n):
        if(i==n-1):
            print(res[i])
        else:
            print(res[i],end=" ")
    