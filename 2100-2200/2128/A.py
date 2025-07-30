t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    cost=0
    ind=-1
    for i in range(n-1,-1,-1):
        if(a[i]<=c):
            ind=i
            break
        else:
            cost+=1
    fact=1
    right=ind
    left=0
    while(left<=right):
        while(right>=0 and a[right]*fact>c):
            right-=1
            cost+=1
        right-=1
        fact*=2
    print(cost)