t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    cost=0
    ind=-1
    for i in range(n-1,-1,-1):
        if(a[i]<c):
            ind=i
            break
        else:
            cost+=1
    fact=1
    left=0
    right=ind
    while(left<=right):
        while(a[right]*fact>c):
            right-=1
            cost+=1
        right-=1
        fact*=2
    print(cost)