t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    leftmin=[0]*(n)
    mini=float('inf')
    for i in range(n):
        mini=min(mini,a[i])
        if(mini==a[i]):
            leftmin[i]=1
    rightmax=[0]*(n)
    maxi=float('-inf')
    for i in range(n-1,-1,-1):
        maxi=max(maxi,a[i])
        if(maxi==a[i]):
            rightmax[i]=1
    
    res=""
    for i in range(n):
        if(leftmin[i]==1 or rightmax[i]==1):
            res+='1'
        else:
            res+='0'
    print(res)
