t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    res=[0]*(n)
    ind=0
    for i in range(n):
        if(i==x):
            res[n-1]=i
        else:
            res[ind]=i
            ind+=1
    for it in res:
        print(it,end=" ")
    print("\n")